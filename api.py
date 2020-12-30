from flask import jsonify

def get_client(json):     return json.get("client")
def get_line(json):       return json.get("line")
def get_session_id(json): return json.get("sessionId")

def create_response(line): return jsonify({"line": line})

def create_api_handler(h):
    def api_handler():
        return lambda json: create_response(h(get_session_id(json), get_line(json)))
    return api_handler
