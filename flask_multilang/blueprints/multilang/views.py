from flask import render_template


def index():
    return render_template('index.html')


def _hello_world_helper():
    return render_template('hello-world.html')


def hello_world_sk():
    return _hello_world_helper()


def hello_world_en():
    return _hello_world_helper()
