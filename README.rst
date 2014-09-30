PyMediaRSS2Gen
==============

A Python library for generating Media RSS 2.0 feeds.


About
-----

This module intents to implement the Media Feed specification version
1.5.1 from Yahoo found at `http://www.rssboard.org/media-rss`__. The
Media RSS specification is a namespace for `RSS 2.0`_.


Usage
-----


Requirements
------------

1. **Python**

   PyMediaRSS2Gen is tested to run on Python starting version 2.6. as it
   requires the OrderedDict module. If you need to run it with Python
   2.6 (or maybe lower, I haven’t tested it) you can use the
   `OrderedDict Backport by Raymond Hettinger`_.

2. **Modules**

   PyMediaRSS2Gen requires the `PyRSS2Gen module`_ on which it is based
   and which gave the initial spark for this module.


Installation
------------

1. Easiest way to install this module is using pip (as soon as it’s
   uploaded to the PyPI)::

       % pip install PyMediaRSS2Gen

2. If you want to install the module manually download the package,
   unzip it and run::

       % cd where/you/put/PyMediaRSS2Gen/
       % python setup.py install

   which uses the standard Python installer. Read the documentation for
   more details about installing Python modules.

3. As this module contains just one Python file you could just copy it
   wherever you need it, e.g. your project directory.


How To Contribute
-----------------

Every open source project lives from the generous help by contributors
that sacrifice their time and PyMediaRSS2Gen is no different.

This project lives on `GitHub`_. You are very welcome to fork this
project and submit pull requests! If you don’t know how to do this you
can still report errors by `opening an issue`_.


Copyright and license
---------------------

| Copyright (c) 2014 Dirk Weise. Code released under the `MIT license`_.
| I’m happy if you drop me a line if this module was usefull for you.


.. __ http://www.rssboard.org/media-rss
.. _RSS 2.0: http://www.rssboard.org/rss-specification
.. _OrderedDict Backport by Raymond Hettinger: http://code.activestate.com/recipes/576693/
.. _PyRSS2Gen module: https://pypi.python.org/pypi/PyRSS2Gen/
.. _download the package: https://pypi.python.org/pypi/PyMediaRSS2Gen/
.. _Read the documentaion: https://docs.python.org/install/index.html
.. _pet project on GitHub: https://github.com/wedi/PyMediaRSS2Gen
.. _open an issue: https://github.com/wedi/PyMediaRSS2Gen/issues
.. _GitHub: https://github.com/wedi/PyMediaRSS2Gen/
.. _opening an issue: https://github.com/wedi/PyMediaRSS2Gen/issues/
.. _MIT license: https://github.com/wedi/PyMediaRSS2Gen/blob/master/LICENSE.txt
