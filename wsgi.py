#!/usr/bin/env python
from wsgiref.simple_server import make_server

from flask_multilang.app import app as application


if __name__ == '__main__':
    httpd = make_server('localhost', 8051, application)
    httpd.serve_forever()
