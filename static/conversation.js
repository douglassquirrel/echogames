game_selector = get_element("games");
transcript    = get_element("transcript");
line_input    = get_element("line_input");
send_button   = get_element("send_button");

function print(line) { append(transcript, line + LINE_BREAK); }

function send_line() {
    line = line_input.value;

    print(line);
    erase(line_input);

    send_request(game_selector.value, line, print);
}

call_on_click(send_button, send_line);
click_on_enter(line_input, send_button);
