#!/usr/bin/python
# -*- coding: utf-8 -*-
import coverage
import unittest

# define coverage to check app module

c = coverage.coverage(branch=True, include='geocoder/*')
c.start()

# discover finds tests in 'tests' folder

suite = unittest.TestLoader().discover('geocoder/tests')
unittest.TextTestRunner(verbosity=2).run(suite)

c.stop()
c.report()
