import json
import os

from flask import g, request


current_dir = os.path.dirname(__file__)
messages_json = os.path.join(current_dir, 'data/messages.json')


with open(messages_json, encoding='utf-8', mode='r') as f:
    messages = json.load(f)


def get_translation(message, lang):
    if lang == 'sk':
        return message

    return messages[message][lang]


def get_current_lang():
    return g.lang if hasattr(g, 'lang') else get_lang_from_url()


def get_lang_from_url():
    return request.path.split('/')[1]


def translate_message(message):
    lang = get_current_lang()
    return get_translation(message, lang=lang)
