from alexa import setup_alexa
from api import create_response, get_client, get_line, get_session_id
from flask import Flask, abort, render_template, request
from flask_ask_sdk.skill_adapter import SkillAdapter
from games import find_handler, games

app = Flask(__name__)
skill_adapter = setup_alexa(app)

@app.route('/alexagames/agree', methods=['POST'])
def invoke_skill():
    return skill_adapter.dispatch_request()

@app.route('/games/<game>/', methods=['POST'])
def post_line(game):
    json = request.get_json()
    print(json)

    handler = find_handler(game)
    if handler:
        line = handler(get_session_id(json), get_line(json))
        return create_response(line)
    else:
        print(f"Unknown game: {game}")
        abort(404)

@app.route('/')
def root():
    return render_template('index.html', games=games)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
