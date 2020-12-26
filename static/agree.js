function send_line() {
    line_input = document.getElementById("line_input");
    transcript = document.getElementById("transcript");

    line = line_input.value;
    document.getElementById("transcript").innerHTML += line + "<br/>";

    line_input.value = "";
}
