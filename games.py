from alexa import create_alexa_handler
from api import create_api_handler
from db import get_conversation, store_line
from game_random import nth_random
from util import compare, first_match, to_digits

def agree(session_id, line):
    store_line(session_id, line)
    response = "I agree!"
    store_line(session_id, response)
    return response

def disagree(session_id, line):
    store_line(session_id, line)
    response = "No way!"
    store_line(session_id, response)
    return response

def echo(session_id, line):
    store_line(session_id, line)
    response = line
    store_line(session_id, response)
    return response

def guess(session_id, line):
    store_line(session_id, line)

    conversation = get_conversation(session_id)
    guess = to_digits(line)
    seed = to_digits(session_id)
    target = nth_random(seed, 1, 100, 1)
    turns = len(conversation)//2 + 1

    results = {-1:"too low", 0:f"CORRECT in {turns} turns", 1:"too high"}
    result = results[compare(guess, target)]

    response = f"Guess a number 1-100. Your guess of {guess} is {result}!"
    store_line(session_id, response)
    return response

handlers = None
def init_games(app):
    global handlers
    games = [agree, disagree, echo, guess]
    def create_handlers(g): return {"API": create_api_handler(g), "alexa": create_alexa_handler(g, app)}
    handlers = {g.__name__: create_handlers(g) for g in games}

def find_handler(client, path):
    if not client or client != "API":
        client = "alexa" 
    g = handlers.get(path)
    return None if not g else g[client]

def list_games():
    games = handlers.keys() 
    return [{"path": g, "name": g.capitalize()} for g in games]
