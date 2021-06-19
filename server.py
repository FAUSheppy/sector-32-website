#!/usr/bin/python3
import flask
from flask.ext.scss
import requests
import argparse
import datetime
import itertools
import json
import os

app = flask.Flask("Sector 32 Web")

@app.route('/')
def leaderboard():
    finalResponse = flask.render_template("base.html")
    return finalResponse

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.before_first_request
def init():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Start Sector 32 -Web',
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--interface', default="localhost",
            help='Interface on which flask (this server) will take requests on')
    parser.add_argument('--port', default="5002",
            help='Port on which flask (this server) will take requests on')

    args = parser.parse_args()
    
    flask.ext.scss.Scss(app)
    app.config.from_object("config")

    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(host=args.interface, port=args.port)
