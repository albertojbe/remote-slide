from flask import Flask
from flask.templating import render_template
import pyautogui

import utils

app = Flask(__name__)

@app.route("/")
def index():
    ip = utils.get_ip()
    print(ip)
    return render_template('index.html', ip=ip)

@app.route("/button/<key>")
def pressKey(key: str):
    print(key)
    pyautogui.hotkey(key)
    return {'status': 'ok'}
