# coding: utf-8

import config
import os
import requests as consumer
from flask import (
    Flask, request, jsonify, render_template, redirect, url_for
)

app = Flask('slack-invite')


@app.route('/')
def index():
    if not config.BG_FILENAME:
        config.BG_FILENAME = url_for('static', filename='img/bg.jpg')
    return render_template('index.html', config=config)


@app.route('/invite', methods=['GET', 'POST', ])
def invite():
    if request.method == 'POST':
        data = {
            'email': request.values['email'],
            'token': config.SLACK_TOKEN,
            'set_active': 'true',
        }

        c = consumer.post(
            '%s/api/users.admin.invite' % config.SLACK_URL,
            params=data
        ).json()

        return render_template('invite.html', config=config, data=c)
    else:
        return redirect('/')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
