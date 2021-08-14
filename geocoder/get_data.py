#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import current_app
from math import sin, cos, sqrt, atan2, radians
import requests
import json

# approximate radius of earth in km

R = 6378.0

# Center of the MKAD coordinate for calc distance

mkad_lat = 55.755821
mkad_lon = 37.617635


def distance(place, lat, lon):

    # if it is in MKAD coordinates, calculation is not performed.

    if lat <= 55.917 and lat >= 55.503 and lon >= 37.329 and lon \
        <= 37.895:
        return 'Thats place in MKAD.'
    else:
        lat1 = radians(mkad_lat)
        lon1 = radians(mkad_lon)
        lat2 = radians(lat)
        lon2 = radians(lon)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) \
            ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return 'Distance from Mkad to %s ' % place \
            + str(round(distance, 2)) + ' km.'


def get_geo(adress):
    if adress == '':
        return 'You should enter the place/coordinate'
    elif adress is None:
        return ''
    destination_req = \
        requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=%s&format=json&geocode='
                      % current_app.config['BEST_API_KEY'] + adress
                     + '&lang=en-US')
    data_destination = destination_req.json()
    if data_destination['response']['GeoObjectCollection'
                                    ]['metaDataProperty'
            ]['GeocoderResponseMetaData']['found'] == '0':
        return 'I guess there is no such place'
    else:
        destination_coordinate = data_destination['response'
                ]['GeoObjectCollection']['featureMember'][0]['GeoObject'
                ]['Point']['pos']
        destination_coordinate = destination_coordinate.split(' ')
        return distance(adress, float(destination_coordinate[1]),
                        float(destination_coordinate[0]))
