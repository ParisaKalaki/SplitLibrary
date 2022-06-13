# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 11:20:44 2022

@author: paris
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="split-library",
    version="0.1.0",
    description="split library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Parisa",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["split_library"],
    include_package_data=True,
    install_requires=["numpy==1.20.2"],
    tests_require=['pytest']
)