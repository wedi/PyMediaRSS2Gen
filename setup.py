# coding=utf-8
"""Setup script to install PyMediaRSS2Gen."""

import sys
from distutils.core import setup

if sys.version_info < (2, 7):
    version_dep_reqs = ['ordereddict']
else:
    version_dep_reqs = []

try:
    long_description = \
        open('README.rst').read() + '\n\n' + \
        open('CHANGELOG.rst').read() + '\n\n' + \
        open('AUTHORS.rst').read()
except (OSError, IOError):
    long_description = ''

setup(
    name='PyMediaRSS2Gen',
    version='0.1.0',
    description='A Python library for generating Media RSS 2.0 feeds.',
    long_description=long_description,
    author='Dirk Weise',
    author_email='code@dirk-weise.de',
    license='MIT',
    url='https://github.com/wedi/PyMediaRSS2Gen',
    download_url='https://github.com/wedi/limit-login-countries/archive/0.1.0.tar.gz',  # noqa
    keywords=['RSS', 'Feed'],
    install_requires=['PyRSS2Gen'].extend(version_dep_reqs),
    py_modules=['PyMediaRSS2Gen'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License'
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: XML",
    ],
)
