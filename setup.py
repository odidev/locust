# -*- coding: utf-8 -*-
import ast
import os
import re
import sys

from setuptools import find_packages, setup

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

setup(
    name="locust",
    install_requires=[
        "gevent",
        "flask",
        "Werkzeug",
        "requests",
        "msgpack",
        "pyzmq",
        "geventhttpclient",
        "ConfigArgParse",
        "psutil",
        "Flask-BasicAuth",
        "Flask-Cors",
        "roundrobin",
        "typing-extensions",
    ],
    test_suite="locust.test",
    tests_require=[
        "cryptography",
        "mock",
        "pyquery",
    ],
    extras_require={
        ":sys_platform == 'win32'": ["pywin32"],
    },
    use_scm_version={
        "write_to": "locust/_version.py",
        "local_scheme": "no-local-version",
    },
    setup_requires=["setuptools_scm"],
)
