from alexa import setup_alexa
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
    request_json = request.get_json()
    print(request_json)

    handler = find_handler(game)
    if handler:
        return handler(request_json)
    else:
        print(f"Unknown game: {game}")
        abort(404)

@app.route('/')
def root():
    return render_template('index.html', games=games)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
