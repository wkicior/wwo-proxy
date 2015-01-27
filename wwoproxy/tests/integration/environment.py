from wwoproxy.boundary.wwo import app
from flask import request
import threading
import requests
import os



def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown')
def shutdown():
    shutdown_server()


def before_all(context):
    context.server = app
    context.thread = threading.Thread(target=app.run)
    context.thread.start()


def after_all(context):
    requests.get('http://localhost:5000/shutdown')
