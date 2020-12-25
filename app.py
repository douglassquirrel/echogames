# app.py
from flask import Flask, request, jsonify, send_file
app = Flask(__name__)

@app.route('/agree/', methods=['POST'])
def post_line():
    request_json = request.get_json()
    print(request_json)
    return jsonify({"version": "1.0", "response": {"outputSpeech": {"type": "PlainText", "text": "I agree!"}}})

@app.route('/')
def root():
    print("In the root!")
    return send_file('index.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
