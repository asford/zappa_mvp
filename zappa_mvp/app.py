from flask import Flask

from .greeting import get_greeting

app = Flask(__name__)


@app.route("/")
def index():
    """Return greeting."""
    return get_greeting(), 200
