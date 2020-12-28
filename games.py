from flask import jsonify

def decode(json):
    return json["request"]["intent"]["slots"]["line"];

def create_response(text):
    return jsonify({"version": "1.0", "response": {"outputSpeech": {"type": "PlainText", "text": text}}})

def agree(json):
    return create_response("I agree!");

def disagree(json):
    return create_response("No way!");

def echo(json):
    line = decode(json);
    return create_response(line);

def guess(json):
    return create_response("Wrong!");

games = [{"name": "Agree",    "path": "agree",    "handler": agree   },
         {"name": "Disagree", "path": "disagree", "handler": disagree},
         {"name": "Echo",     "path": "echo",     "handler": echo   }, 
         {"name": "Guess",    "path": "guess",    "handler": guess   }, 
        ]

def find_handler(path):
    matches = iter([g["handler"] for g in games if g["path"] == path])
    return next(matches, None)
