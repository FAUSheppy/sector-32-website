#!/usr/bin/python3
import flask
import requests
import argparse
import datetime
import itertools
import json
import os

app = flask.Flask("Sector 32 Web")

@app.route('/')
def leaderboard():

    return flask.render_template("base.html", config=app.config)

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.before_first_request
def init():
    app.config.from_object("config")
    params = "?x=1920&y=1080&encoding=webp"
    for i in range(0, len(app.config["PARALAX_LAYERS"])):
        app.config["PARALAX_LAYERS"][i] = app.config["PARALAX_LAYERS"][i] + params

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Start Sector 32 -Web',
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--interface', default="localhost",
            help='Interface on which flask (this server) will take requests on')
    parser.add_argument('--port', default="5002",
            help='Port on which flask (this server) will take requests on')

    args = parser.parse_args()
    
    app.config.from_object("config")

    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(host=args.interface, port=args.port)
