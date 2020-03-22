#!/usr/bin/env python
from setuptools import find_packages
from distutils.core import setup

setup(name='cluttermanager',
      version='0.2.0',
      description='Clutter Manager for your folders',
      author='Puneet Saini',
      author_email='puneet29saini@gmail.com',
      url='https://github.com/puneet29/ClutterManager',
      packages=find_packages(exclude=['*.pyc']),
      scripts=['./bin/cluttermanager'],
      )