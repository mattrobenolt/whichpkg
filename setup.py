#!/usr/bin/env python
"""
whichpkg
========
Locate the path of a specific python module
"""

from setuptools import setup

setup(
    name='whichpkg',
    version='0.3.0',
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/whichpkg',
    description='Locate the path of a specific python module',
    long_description=__doc__,
    install_requires=[],
    scripts=['bin/whichpkg'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
