import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def store_line(session_id, line):
    conn = psycopg2.connect(DATABASE_URL) #, sslmode='require')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS conversations (id serial PRIMARY KEY, session_id varchar, line varchar);")
    cur.execute("INSERT INTO conversations (session_id, line) VALUES (%s, %s)", (session_id, line))
    conn.commit()
    cur.close()    
    conn.close()
