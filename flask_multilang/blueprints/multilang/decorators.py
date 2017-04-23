from flask import current_app, g, request, url_for

from .exceptions import SwitchLanguage, Basic404, UnsupportedLanguage
from flask_multilang.messages import get_lang_from_url


def verify_lang():
    actual_lang = get_lang_from_url()
    required_lang = request.endpoint.split('_')[-1]

    # don't check language for endpoints which don't require it
    # (e.g. when handling an unknown language exception)
    if required_lang not in current_app.config['LOCALE_SUPPORTED']:
        return

    # prepare the URL for new language and raise an Exception which
    # will redirect to next URL as redirecting from here doesn't work
    if actual_lang != required_lang and g.lang == actual_lang:
        new_enpoint = request.endpoint.replace(required_lang, actual_lang)
        query_string = request.query_string.decode('utf-8')

        next_url = url_for(new_enpoint, **request.view_args)

        if query_string:
            next_url += '?{q}'.format(q=query_string)

        raise SwitchLanguage(next_url)

    if actual_lang != required_lang:
        raise Basic404


def set_app_language(endpoint, values):
    lang = request.cookies.get('lang')

    if lang:
        values['lang'] = lang
    else:
        values.setdefault('lang', current_app.config['LOCALE_DEFAULT'])


def get_app_language(endpoint, values):
    lang = values.pop('lang', current_app.config['LOCALE_DEFAULT'])
    if lang not in current_app.config['LOCALE_SUPPORTED']:
        raise UnsupportedLanguage

    g.lang = lang
