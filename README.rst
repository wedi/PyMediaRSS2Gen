PyMediaRSS2Gen
==============

A Python library for generating Media RSS 2.0 feeds.


About
-----

This module intents to implement the `Media Feed specification`_ from Yahoo.
The Media RSS specification is a namespace for `RSS 2.0`_. To accomplish this
task it relies heavily on the `PyRSS2Gen module`_. As you might guess this
Media RSS module is even nameded after its role model.

Right now this is considered **ALPHA**! *Breaking backwards compatibility is
possible at any time*, I will **try** to avoid it though. I started off with a
base which can be extended as needed or as we (you and me) have time. See below
for a list with specification details and their current implementation status.
This way I keep track of what needs to be done and users can see what they can
accomplish out of the box and what requires some contributions. Feel free to
fork the project, implement a missing feature and send a pull request.


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


Status and Todo
---------------

Tests are missing completely so automated testing with tox is a todo item! I'm
still new to python and haven't figured out testing yet.

Below you find the implementation status of the Media RSS elements
according to the `Media Feed specification`_.

+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
|             Feature              |          Status         |                                 Issue on GitHub                                  |
+==================================+=========================+==================================================================================+
| media:content                    | Ready                   |                                                                                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:text                       | Ready                   |                                                                                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:title                      | Ready                   |                                                                                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:group                      | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/1>`__                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| Enable elements on channel level | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/3>`__                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:rating                     | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/2>`__                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:description                | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/4>`__                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:keywords                   | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/5>`__                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:thumbnail                  | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/6>`__                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:category                   | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/7>`__                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:hash                       | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/8>`__                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:player                     | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/9>`__                  |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:credit                     | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/10>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:copyright                  | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/11>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:restriction                | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/12>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:community                  | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/13>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:comments                   | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/14>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:embed                      | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/15>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:responses                  | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/16>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:backLinks                  | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/17>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:status                     | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/18>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:price                      | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/19>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:license                    | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/20>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:subTitle                   | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/21>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:peerLink                   | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/22>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:location                   | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/23>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:rights                     | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/24>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| media:scenes                     | Not implemented         | `See issue <https://github.com/wedi/PyMediaRSS2Gen/issues/25>`__                 |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+
| **Summary**                      | **3 of 28 implemented** | `See all issues <https://github.com/wedi/PyMediaRSS2Gen/labels/specification>`__ |
+----------------------------------+-------------------------+----------------------------------------------------------------------------------+


Copyright and license
---------------------

| Copyright (c) 2014 Dirk Weise. Code released under the `MIT license`_.
| I’m happy if you drop me a line if this module was usefull for you.


.. _Media Feed specification: http://www.rssboard.org/media-rss
.. _RSS 2.0: http://www.rssboard.org/rss-specification
.. _PyRSS2Gen module: https://pypi.python.org/pypi/PyRSS2Gen/
.. _OrderedDict Backport by Raymond Hettinger: http://code.activestate.com/recipes/576693/
.. _download the package: https://pypi.python.org/pypi/PyMediaRSS2Gen/
.. _Read the documentaion: https://docs.python.org/install/index.html
.. _pet project on GitHub: https://github.com/wedi/PyMediaRSS2Gen
.. _open an issue: https://github.com/wedi/PyMediaRSS2Gen/issues
.. _GitHub: https://github.com/wedi/PyMediaRSS2Gen/
.. _readme about contributions: https://github.com/wedi/PyMediaRSS2Gen/blob/master/CONTRIBUTING.rst
.. _opening an issue: https://github.com/wedi/PyMediaRSS2Gen/issues/
.. _MIT license: https://github.com/wedi/PyMediaRSS2Gen/blob/master/LICENSE.txt
