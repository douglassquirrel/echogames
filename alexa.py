from ask_sdk_core.dispatch_components import AbstractExceptionHandler, AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard
from flask_ask_sdk.skill_adapter import SkillAdapter, VERIFY_SIGNATURE_APP_CONFIG, VERIFY_TIMESTAMP_APP_CONFIG
from os import environ
from util import arbitrary_dict_element

def init_alexa(app):
    app.config.setdefault(VERIFY_SIGNATURE_APP_CONFIG, False) 
    app.config.setdefault(VERIFY_TIMESTAMP_APP_CONFIG, False) 

def make_response(handler_input, response, end_session_flag):
    handler_input.response_builder.speak(response) \
            .set_card(SimpleCard("EchoGames", response)) \
            .set_should_end_session(end_session_flag)
    return handler_input.response_builder.response

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return make_response(handler_input, "Welcome to the game!", False)

class IntentHandler(AbstractRequestHandler):
    def __init__(self, game, name):
        self.game = game
        self.name = name

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name(self.name + "Intent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        re = handler_input.request_envelope
        session_id = re.session.session_id
        slots = re.request.intent.slots
        print("Slots:", type(slots), slots)
        if not slots:
            line = "FOO"
        else:
            line = arbitrary_dict_element(slots).value
        response = self.game(session_id, line)

        return make_response(handler_input, response, True)

class AllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        print("Exception:", exception)

        response = "Sorry, I didn't understand. Please try again!"
        handler_input.response_builder.speak(response).ask(response)
        return handler_input.response_builder.response

def create_alexa_handler(game, name, app):
    ALEXA_SKILL_ID = environ["ALEXA_SKILL_ID"]

    sb = SkillBuilder()
    sb.add_request_handler(LaunchRequestHandler())
    sb.add_request_handler(IntentHandler(game, name))
    sb.add_exception_handler(AllExceptionHandler())

    sa = SkillAdapter(skill=sb.create(), skill_id=ALEXA_SKILL_ID, app=app)

    def alexa_handler(): 
        return lambda json: sa.dispatch_request()
    return alexa_handler
    
