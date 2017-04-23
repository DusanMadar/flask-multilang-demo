from flask import Flask, redirect, url_for

from config import config
from .blueprints import Multilang


app = Flask(__name__)
app.config.from_object(config)

multilang = Multilang()
multilang.prepare()
app.register_blueprint(multilang.blueprint)


@app.route('/')
def index():
    return redirect(url_for('multilang.index'))
