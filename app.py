# coding: utf-8

from flask import Flask, request, jsonify, render_template
import requests as consumer
import config

app = Flask('slack-invite')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/invite', methods=['POST',])
def invite():
    data = {
        'email': request.values['email'],
        'token': config.SLACK_TOKEN,
        'set_active': 'true',
    }

    c = consumer.post(
        '%s/api/users.admin.invite' % config.SLACK_URL,
        params=data
    ).json()

    return render_template('invite.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
