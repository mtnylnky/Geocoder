#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from flask import url_for

from geocoder import init_app


class SiteTestCase(unittest.TestCase):

    def setUp(self):
        """
        Creates app environment with test settings.
        """
        self.app = init_app()
        self.client = self.app.test_client()
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()

    def tearDown(self):
        pass

    def test_site_avaliable(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_place_empty(self):
        resp = self.client.get('/?distance=')
        assert b'enter the place' in resp.data
    
    def test_place_name(self):
        resp = self.client.get('/?distance=Adana')
        assert b'Adana' in resp.data
    
    def test_coordinate(self):
        resp = self.client.get('/?distance=1,1')
        assert b'1,1' in resp.data
    
    def test_wrong_query(self):
        resp = self.client.get('/distance=Moscow')
        self.assertEqual(resp.status_code, 404)
    
    def test_wrong_page(self):
        resp = self.client.get('/distance')
        self.assertEqual(resp.status_code, 404)

if __name__ == '__main__':
    unittest.main()