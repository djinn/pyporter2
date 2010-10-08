#!/usr/bin/env python

"""
setup.py file for FreeLing extension
"""

from distutils.core import setup, Extension


setup (name = 'pyporter2',
       version = '0.1',
       author      = "mdirolf <mike@dirolf.com>",
       description = """Snowball stemmer""",
       packages = ['pyporter2'],
       package_data = {'pyporter2':['voc.txt', 'stemmedvoc.txt']},
       )
