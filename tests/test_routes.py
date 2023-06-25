from flask import Flask, render_template
from modules import modules


def test_index():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "I'm alive"

    app.testing = True
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
