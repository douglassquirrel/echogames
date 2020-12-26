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
    document.getElementById("transcript").innerHTML += line + "<br/>";

    line_input.value = "";
}
