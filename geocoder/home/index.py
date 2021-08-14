#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, render_template, request, jsonify
from flask import current_app, url_for, redirect
import logging
from geocoder.get_data import get_geo

Index = Blueprint('Index', __name__, template_folder='templates',
                  static_folder='static',
                  static_url_path='/geocoder/home/static')


@Index.before_request
def log_request_info():
    logging.basicConfig(filename='geocoder.log', encoding='utf-8',
                        level=logging.DEBUG)  # log configuration


@Index.route('/', methods=['GET', 'POST'])
def index():
    title = 'Geocoder'
    if request.method == 'POST':

        # If the form is used, the data will be processed with the post method.

        distance = request.form.get('distance')  # Get variable for post
        distance = get_geo(distance)  # Send to calc function
        current_app.logger.info(distance)  # Add .log file
        return render_template('index.html', distance=distance,
                               title=title)  # return index with data
    elif request.method == 'GET':

        # In case of using http, the data will be processed with get

        distance = request.args.get('distance')  # get variable for get
        distance = get_geo(distance)
        current_app.logger.info(distance)
        return render_template('index.html', distance=distance,
                               title=title)

    # returns index if the page is opened for the first time

    return render_template('index.html', distance='', title=title)
