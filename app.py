# coding: utf-8

from flask import Flask, request, jsonify

app = Flask('slack-invite')

@app.route('/')
def index():
    return "Hello World!", 200

@app.route('/invite')
def invite():
    return jsonify({'a': 'a'})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)