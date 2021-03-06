#!/usr/bin/env python

from setuptools import setup

import genetix


extras = {
    'develop': [
        'pytest',
        'fuzzywuzzy==0.8.0',
        'python-Levenshtein==0.12.0'
    ]
}

setup(
    name="genetix-py",
    version=genetix.__version__,
    description=genetix.__doc__,
    url="https://github.com/ryanleland/Genetix.py",
    author=genetix.__author__,
    packages=[
        'genetix'
    ],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    license=open("LICENSE").read(),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ),
    extras_require=extras
)
