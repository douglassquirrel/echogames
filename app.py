from api import get_client
from flask import Flask, abort, render_template, request
from games import find_handler, init_games, list_games

app = Flask(__name__)
init_games(app)

@app.route('/games/<game>/', methods=['POST'])
def post_line(game):
    json = request.get_json()
    print(json)

    client = get_client(json)
    handler = find_handler(client, game)
    if handler:
        if not client or client != "API":
            return handler.dispatch_request()
        else:
            return handler(json)
    else:
        print(f"Unknown game: {game}")
        abort(404)

@app.route('/')
def root():
    return render_template('index.html', games=list_games())

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
