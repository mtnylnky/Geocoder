#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Application entry point."""

from geocoder import init_app

app = init_app()

if __name__ == '__main__':
    app.run(debug=True)
