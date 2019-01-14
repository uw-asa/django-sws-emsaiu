#!/usr/bin/env python

import os
from setuptools import setup

PACKAGE = 'emsaiu'

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# The VERSION file is created by travis-ci, based on the tag name
version_path = os.path.join(PACKAGE, 'VERSION')
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='Django-SWS-EMSAIU',
    version=VERSION,
    packages=[PACKAGE],
    include_package_data=True,
    install_requires = [
        'AuthZ-Group',
        'Django>=1.11.18,<2.0',
        'django-compressor',
        'Django-SupportTools<3.0 ; python_version < "3.0"',
        'Django-SupportTools ; python_version >= "3.0"',
        'UW-EMS-Client',
        'UW-RestClients-GWS<2.0 ; python_version < "3.0"',
        'UW-RestClients-GWS ; python_version >= "3.0"',
        'UW-RestClients-SWS<2.0 ; python_version < "3.0"',
        'UW-RestClients-SWS ; python_version >= "3.0"',

    ],
    license='Apache License, Version 2.0',
    description='Django app to aid in the import of the academic schedule from the UW Student Web Service',
    long_description=README,
    url='https://github.com/uw-it-cte/django-sws-emsaiu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
)
