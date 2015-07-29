# coding: utf-8

from flask import Flask, request

app = Flask('slack-invite')

@app.route("/")
def index():
    return "Hello World!", 200

app.run(debug=True, use_reloader=True)