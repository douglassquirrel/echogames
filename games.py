from db import get_conversation, store_line
from flask import jsonify
from game_random import nth_random
from util import compare, first_match, to_digits

def get_line(json):
    return json["request"]["intent"]["slots"]["line"]
def get_session(json):
    return json["session"]["sessionId"]

def create_response(text):
    return jsonify({"version": "1.0", "response": {"outputSpeech": {"type": "PlainText", "text": text}}})

def agree(json):
    return create_response("I agree!")

def disagree(json):
    print("disagree!")
    return create_response("No way!")

def echo(json):
    line = get_line(json)
    session_id = get_session(json)
    store_line(session_id, line)
    store_line(session_id, line)
    return create_response(line)

def guess(json):
    line = get_line(json)
    session_id = get_session(json)
    conversation = get_conversation(session_id)
    store_line(session_id, line)

    guess = to_digits(line)
    seed = to_digits(session_id)
    target = nth_random(seed, 1, 100, 1)
    turns = len(conversation)//2 + 1
    results = {-1:"too low", 0:f"CORRECT in {turns} turns", 1:"too high"}
    result = results[compare(guess, target)]

    response = f"Guess a number 1-100. Your guess of {guess} is {result}!"
    store_line(session_id, response)
    return create_response(response)

games = [{"name": "Agree",    "path": "agree",    "handler": agree   },
         {"name": "Disagree", "path": "disagree", "handler": disagree},
         {"name": "Echo",     "path": "echo",     "handler": echo   }, 
         {"name": "Guess",    "path": "guess",    "handler": guess   }, 
        ]

def find_handler(path):
    g = first_match(games, lambda g: g["path"] == path)
    return g["handler"] if g else None
