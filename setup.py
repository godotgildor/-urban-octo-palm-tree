#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from setuptools import setup, find_namespace_packages

current_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(current_dir, "requirements_dev.txt")) as reqs_file:
    requirements_dev = reqs_file.readlines()

install_requires = requirements_dev

setup(
    name="urban-octo-palm-tree",
    version="1.0.0",
    author="Brett T. Hannigan",
    classifiers=[
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython"
    ],
    description="Dummy package",
    long_description="Dummy Package for testing CI",
    include_package_data=True,
    install_requires=install_requires,
    extras_require={},
    packages=find_namespace_packages(include=["urban_octo_palm_tree.*"]),
    test_suite="pytest",
    tests_require=requirements_dev,
)
