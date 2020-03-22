#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='cluttermanager',
      long_description=long_description,
      long_description_content_type="text/markdown",
      version='0.4.7',
      description='Clutter Manager for your folders',
      author='Puneet Saini',
      author_email='puneet29saini@gmail.com',
      url='https://github.com/puneet29/ClutterManager',
      packages=find_packages(exclude=['*.pyc']),
      scripts=['./bin/cluttermanager'],
      )
