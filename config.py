# lang codes
ENGLISH = 'en'
SLOVAK = 'sk'


class Config(object):
    DEBUG = True

    LOCALE_DEFAULT = SLOVAK
    LOCALE_SUPPORTED = [ENGLISH, SLOVAK]


config = Config()
