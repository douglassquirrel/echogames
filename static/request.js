function is_done(request)       { return request.readyState === XMLHttpRequest.DONE; }
function is_ok(request)         { return request.status === 200; }
function is_successful(request) { return (is_done(request) && is_ok(request)); } 

function create_http_request(url, handler) {
    request = new XMLHttpRequest();
    request.open("POST", url);
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    request.onreadystatechange = handler;
    return request;
}    

function parse_response(request) {
    text = request.responseText;
    return JSON.parse(text);
}
