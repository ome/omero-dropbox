#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Copyright 2008-2019 The Open Microscopy Environment, Glencoe Software, Inc.
   All rights reserved.

   Use is subject to license terms supplied in LICENSE.txt

"""

import glob
import sys
import os

from setuptools import setup

VERSION = "5.5.dev1"

url = 'https://docs.openmicroscopy.org/latest/omero/developers/Server/FS.html'


def read(fname):
    """
    Utility function to read the README file.
    :rtype : String
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name="omero-dropbox",
      version=VERSION,
      description="OMERO.dropbox server for watching directories",
      long_description=read("README.rst"),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 '
        'or later (GPLv2+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],  # Get strings from
          # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      author="The Open Microscopy Team",
      author_email="ome-devel@lists.openmicroscopy.org.uk",
      url=url,
      package_dir={"": "src"},
      packages=[''],
      install_requires=[
          "omero-py",  # requires Ice (use wheel for faster installs)
      ],
      tests_require=['pytest<3'])
