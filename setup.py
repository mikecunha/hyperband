#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='hyperband',
      version='0.0.1',
      description='Code for tuning hyperparams with Hyperband',
      packages=find_packages(),
      install_requires=['hyperopt', 'numpy']
)
