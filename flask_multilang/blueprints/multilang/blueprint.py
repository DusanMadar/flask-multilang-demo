from flask import Blueprint

from . import exceptions, decorators, views
from flask_multilang.messages import translate_message


class Multilang(object):
    def __init__(self):
        self.blueprint = Blueprint(
            'multilang',
            __name__,
            url_prefix='/<lang>',
            template_folder='templates',
            static_folder='static'
        )

    def _add_decorators(self):
        self.blueprint.before_request(decorators.verify_lang)
        self.blueprint.url_defaults(decorators.set_app_language)
        self.blueprint.url_value_preprocessor(decorators.get_app_language)

    def _add_exceptions(self):
        self.blueprint.register_error_handler(
            exceptions.SwitchLanguage, exceptions.switch_language
        )
        self.blueprint.register_error_handler(
            exceptions.Basic404, exceptions.basic_404
        )
        self.blueprint.register_error_handler(
            exceptions.UnsupportedLanguage, exceptions.unsupported_language
        )

    def _add_routes(self):
        self.blueprint.add_url_rule(
            '/', view_func=views.index
        )
        self.blueprint.add_url_rule(
            '/ahoj-svet', view_func=views.hello_world_sk
        )
        self.blueprint.add_url_rule(
            '/hello-world', view_func=views.hello_world_en
        )

    def _update_jinja_context(self):
        context = {
            'translate': translate_message,
        }

        return context

    def prepare(self):
        self._add_decorators()
        self._add_exceptions()
        self._add_routes()

        self.blueprint.context_processor(self._update_jinja_context)
