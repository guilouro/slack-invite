# coding: utf-8

from flask import (
    Flask, request, jsonify, render_template, redirect
)
import requests as consumer
import config

app = Flask('slack-invite')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/invite', methods=['GET', 'POST', ])
def invite():
    # import ipdb; ipdb.set_trace()
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

        return render_template('invite.html')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
