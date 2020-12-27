from flask import jsonify

def create_response(text):
    return jsonify({"version": "1.0", "response": {"outputSpeech": {"type": "PlainText", "text": text}}})

def agree(json):
    return create_response("I agree!");

def disagree(json):
    return create_response("No way!");

games = [{"name": "Agree",    "path": "agree",    "handler": agree},
         {"name": "Disagree", "path": "disagree", "handler": disagree},
        ]

def find_handler(path):
    matches = iter([g["handler"] for g in games if g["path"] == path])
    return next(matches, None)
