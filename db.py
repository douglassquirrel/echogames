from os import environ
from psycopg2 import connect
from util import flatten

DATABASE_URL = environ['DATABASE_URL']

CREATE_DB        = """CREATE TABLE IF NOT EXISTS conversations
                      (id SERIAL PRIMARY KEY, 
                       session_id VARCHAR, 
                       line VARCHAR,
                       created_at TIMESTAMPTZ NOT NULL DEFAULT NOW())"""
INSERT_LINE      = "INSERT INTO conversations (session_id, line) VALUES (%s, %s)"
GET_CONVERSATION = "SELECT line FROM conversations WHERE session_id = %s"

def run_sql(sql, args):
    connection = connect(DATABASE_URL) 
    cursor = connection.cursor()

    cursor.execute(CREATE_DB)
    connection.commit()

    cursor.execute(sql, args)
    connection.commit()
    result = cursor.fetchall() if cursor.description else []

    cursor.close()
    connection.close()
    return result

def store_line(session_id, line):
    run_sql(INSERT_LINE, (session_id, line))

def get_conversation(session_id):
    return flatten(run_sql(GET_CONVERSATION, (session_id,)))

def wrap_handler(h):
    def wrapped_handler(session_id, line):
        store_line(session_id, line)
        conversation = get_conversation(session_id)

        response = h(session_id, conversation)
        store_line(session_id, response)
        return response
    return wrapped_handler
