game_selector = document.getElementById("games");
transcript    = document.getElementById("transcript");
line_input    = document.getElementById("line_input");
send_button   = document.getElementById("send_button");

function is_enter(event) { return event.keyCode === 13; }    
function handle_enter(event) {
    if (!is_enter(event)) { return; }
    event.preventDefault();
    send_button.click();  
}

function print(line) { transcript.innerHTML += line + "<br/>"; }

function erase_line_input() { line_input.value = ""; }

function is_done(request)       { return request.readyState === XMLHttpRequest.DONE; }
function is_ok(request)         { return request.status === 200; }
function is_successful(request) { return (is_done(request) && is_ok(request)); } 

function encode(line) { return JSON.stringify({"request":{"intent":{"slots":{"line": line}}}}); }
function decode(json) { return json.response.outputSpeech.text; }

function parse_response(request) {
    text = request.responseText;
    json = JSON.parse(text);
    return decode(json);
}

function handle_response() {
    if (!is_successful(this)) { return; }
    line = parse_response(this);
    print(line);
}

function make_request(url, handler) {
    request = new XMLHttpRequest();
    request.open("POST", url);
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    request.onreadystatechange = handler;
    return request;
}    

function send_request(game, line) {
    request = make_request("/" + game, handle_response);
    body = encode(line);
    request.send(body);
}    

function send_line() {
    line = line_input.value;
    print(line);
    erase_line_input();
    send_request(game_selector.value, line);
}

line_input.addEventListener("keyup", handle_enter);
send_button.onclick=send_line;
