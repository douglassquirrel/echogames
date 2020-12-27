function encode(line) { return JSON.stringify({"request":{"intent":{"slots":{"line": line}}}}); }
function decode(json) { return json.response.outputSpeech.text; }

function send_request(game, line, print) {
    handle_response = function() {
        if (!is_successful(this)) { return; }
        json = parse_response(this);
        line = decode(json);
        print(line);
    }
    request = create_http_request("/" + game, handle_response);
    body = encode(line);
    request.send(body);
}    
