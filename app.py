# coding: utf-8

import config
import requests as consumer
from jac.contrib.flask import JAC
from flask import (
    Flask, request, jsonify, render_template, redirect
)

app = Flask('slack-invite')
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_OUTPUT_DIR'] = './static/css'
app.config['COMPRESSOR_STATIC_PREFIX'] = '/static/css'
jac = JAC(app)


@app.route('/')
def index():
    return render_template('index.html', group=config.SLACK_GROUP)


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

        return render_template('invite.html')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
