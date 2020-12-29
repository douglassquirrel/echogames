from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard
from flask_ask_sdk.skill_adapter import SkillAdapter

SKILL_ID=12345 #Replace with real ID from environment
sb = SkillBuilder()

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    # type: (HandlerInput) -> Response
    line = "I'm agreeable, say something!"

    handler_input.response_builder.speak(line) \
        .set_card(SimpleCard("Agreeable", line)) \
        .set_should_end_session(False)
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_intent_name("AgreeIntent"))
def agree_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    line = "I agree!"

    handler_input.response_builder.speak(line) \
        .set_card(SimpleCard("Agreeable", line)) \
        .set_should_end_session(True)
    return handler_input.response_builder.response

@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    # type: (HandlerInput, Exception) -> Response
    print(exception)

    line = "Sorry, I didn't understand, so I can't agree. Please try again!"
    handler_input.response_builder.speak(line).ask(line)
    return handler_input.response_builder.response

def setup_alexa(app):
    return SkillAdapter(skill=sb.create(), skill_id=SKILL_ID, app=app)


    