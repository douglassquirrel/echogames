game_selector = document.getElementById("games");
transcript = document.getElementById("transcript");
line_input = document.getElementById("line_input");
send_button = document.getElementById("send_button");

ENTER_KEY_CODE = 13;

line_input.addEventListener("keyup", function(event) {
    if (event.keyCode === ENTER_KEY_CODE) {
        event.preventDefault();
        send_button.click();  
    }
});

function send_line() {
    line = line_input.value;
    transcript.innerHTML += line + "<br/>";
    line_input.value = "";

    request = new XMLHttpRequest();
    url = "/" + game_selector.value;
    request.open("POST", url);
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    request.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            json_response= JSON.parse(this.responseText);
            line = json_response.response.outputSpeech.text;
            transcript.innerHTML += line + "<br/>";
        }
    }
    body = JSON.stringify({"request":{"intent":{"slots":{"line": line}}}});
    request.send(body);
}
