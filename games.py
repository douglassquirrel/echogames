from flask import jsonify;
from game_random import nth_random;
from util import to_digits;

def get_line(json):
    return json["request"]["intent"]["slots"]["line"];
def get_session(json):
    return json["session"]["sessionId"];

def create_response(text):
    return jsonify({"version": "1.0", "response": {"outputSpeech": {"type": "PlainText", "text": text}}})

def agree(json):
    return create_response("I agree!");

def disagree(json):
    return create_response("No way!");

def echo(json):
    line = get_line(json);
    return create_response(line);

def get_result(guess, target):
    if (guess < target):
        return "too low";
    elif (guess > target):
        return "too high";
    else:
        return "CORRECT";

def guess(json):
    guess = to_digits(get_line(json));
    seed = to_digits(get_session(json));
    target = nth_random(seed, 1, 100, 1);
    result = get_result(guess, target);

    response = f"Guess a number 1-100. Your guess of {guess} is {result}!"
    return create_response(response);

games = [{"name": "Agree",    "path": "agree",    "handler": agree   },
         {"name": "Disagree", "path": "disagree", "handler": disagree},
         {"name": "Echo",     "path": "echo",     "handler": echo   }, 
         {"name": "Guess",    "path": "guess",    "handler": guess   }, 
        ]

def find_handler(path):
    matches = iter([g["handler"] for g in games if g["path"] == path])
    return next(matches, None)
