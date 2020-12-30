from ask_sdk_core.dispatch_components import AbstractExceptionHandler, AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard
from flask import request
from flask_ask_sdk.skill_adapter import SkillAdapter, VERIFY_SIGNATURE_APP_CONFIG, VERIFY_TIMESTAMP_APP_CONFIG
from os import environ

def init_alexa(app):
    app.config.setdefault(VERIFY_SIGNATURE_APP_CONFIG, False) 
    app.config.setdefault(VERIFY_TIMESTAMP_APP_CONFIG, False) 

def intent(game): 
    return game.__name__.capitalize() + "Intent"

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        response = "Welcome to the game!"

        handler_input.response_builder.speak(response) \
            .set_card(SimpleCard("Agreeable", response)) \
            .set_should_end_session(False)
        return handler_input.response_builder.response

class IntentHandler(AbstractRequestHandler):
    def __init__(self, game):
        self.game = game

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name(intent(self.game))(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        line = "FOO"
        session_id = handler_input.request_envelope.session.session_id
        response = self.game(session_id, line)

        handler_input.response_builder.speak(response) \
            .set_card(SimpleCard("Agreeable", response)) \
            .set_should_end_session(True)
        return handler_input.response_builder.response

class AllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        print(exception)

        response = "Sorry, I didn't understand. Please try again!"
        handler_input.response_builder.speak(response).ask(response)
        return handler_input.response_builder.response

def create_alexa_handler(game, app):
    ALEXA_SKILL_ID = environ["ALEXA_SKILL_ID"]

    sb = SkillBuilder()
    sb.add_request_handler(LaunchRequestHandler())
    sb.add_request_handler(IntentHandler(game))
    sb.add_exception_handler(AllExceptionHandler())

    sa = SkillAdapter(skill=sb.create(), skill_id=ALEXA_SKILL_ID, app=app)

    def alexa_handler(): 
        return lambda json: sa.dispatch_request()
    return alexa_handler
    
