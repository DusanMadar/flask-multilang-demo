from flask import redirect


class Basic404(Exception):
    pass


class SwitchLanguage(Exception):
    def __init__(self, next_url):
        self.next_url = next_url


class UnsupportedLanguage(Exception):
    pass


def basic_404(e):
    return 'not found', 404


def switch_language(e):
    return redirect(e.next_url)


def unsupported_language(e):
    return 'neznámy jazyk/unknown language', 400
