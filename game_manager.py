from alexa import create_alexa_handler
from api import create_api_handler
from db import wrap_handler

from games.agree    import agree
from games.disagree import disagree
from games.echo     import echo
from games.guess    import guess
games = [agree, disagree, echo, guess]

def path(g): return g.__name__
def name(g): return path(g).capitalize() 

handlers = None
def init_games(app):
    global handlers
    def create_handlers(g):
        w = wrap_handler(g) 
        return {"API":   create_api_handler(w), 
                "alexa": create_alexa_handler(w, name(g), app)}
    handlers = {path(g): create_handlers(g) for g in games}

def find_handler(client, path):
    client = "alexa" if client is None else client
    g = handlers.get(path)
    return None if not g else g[client]

def list_games():
    return [{"path": path(g), "name": name(g)} for g in games]

