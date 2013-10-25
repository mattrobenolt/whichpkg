#!/usr/bin/env python
"""
whichpkg
========
Locate the path of a specific python module
"""

import re
from setuptools import setup

version = re.search("__version__\s*=\s*'(.+)?'", open('bin/whichpkg').read()).groups(1)[0]

setup(
    name='whichpkg',
    version=version,
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
