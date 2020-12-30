function encode(session_id, line) { 
    json = {"client": "API", "sessionId": session_id, "line": line}
    return JSON.stringify(json);
}
function decode(json) { return json.line; }

function send_request(session_id, game, line, print) {
    handle_response = function() {
        if (!is_successful(this)) { return; }
        json = parse_response(this);
        line = decode(json);
        print(line);
    }
    request = create_http_request("/games/" + game, handle_response);
    body = encode(session_id, line);
    request.send(body);
}    
