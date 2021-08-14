#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, Blueprint, current_app
from config import Config


def init_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    with app.app_context():

        # Import all drafts

        from .home import index

        app.register_blueprint(index.Index)  # define 'index' app

    return app
