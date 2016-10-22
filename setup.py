#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys
import os


def check_requirements():
    assert sys.version_info >= (3, 4), "Please use Python 3.4 or higher."
    if os.name == "posix":
        assert os.geteuid() == 0, "Please run with root privileges."

try:
    check_requirements()
    setup(
        name = "icyparser",
        packages = ["icyparser"],
        version = "1.1.0",
        description = "A script to download the ICY information for a stream and return it as a dict",
        author = "Gijs Timmers",
        author_email = "gijs.timmers@student.kuleuven.be",
        url = "https://github.com/GijsTimmers/icyparser",
        keywords = ["shoutcast", "icecast", "stream", "ICY"],
        install_requires = [],
        classifiers = [],
        #entry_points = {
        #    "console_scripts": ["icyparser=icyparser:entry_point"]},
        include_package_data = True
    )
except AssertionError as e:
        print(e)

