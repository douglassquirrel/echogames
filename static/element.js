LINE_BREAK = "<br/>";

function get_element(id) { return document.getElementById(id); }

function get_value(element)      { return element.value; }
function set_value(element, val) { element.value = val;  }
function append(element, text)   { element.innerHTML += text; }
function erase_value(element)    { element.value = ""; }

function call_on_click(element, f) { element.onclick = f; }

function is_enter(event) { return event.keyCode === 13; }    

function click_on_enter(element, button) {
    handle_enter = function(event) {
        if (!is_enter(event)) { return; }
        event.preventDefault();
        button.click();  
    }
    element.addEventListener("keyup", handle_enter);
}

