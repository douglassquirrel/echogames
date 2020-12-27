game_selector = get_element("games");
session_id    = get_element("session_id");
transcript    = get_element("transcript");
line_input    = get_element("line_input");
send_button   = get_element("send_button");

function print(line) { append(transcript, line + LINE_BREAK); }

function send_line() {
    line = get_value(line_input);

    print(line);
    erase_value(line_input);

    send_request(get_value(session_id), get_value(game_selector), line, print);
}

set_value(session_id, "echogames.session." + random(10000, 99999));
call_on_click(send_button, send_line);
click_on_enter(line_input, send_button);
