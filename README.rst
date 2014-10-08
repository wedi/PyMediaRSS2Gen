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

PyMediaRSS2Gen is so far tested to work with Python versions 2.6, 2.7 and 3.4.


Usage
-----

The base class for a media feed is ``MediaRSS2``. It's attributes represent sub
elements, e.g. ``MediaRSS2.copyright`` represents the ``<copyright>`` element
and `MediaRSS2.lastBuildDate`` the ``<lastBuildDate>`` element.

For simple elements which contain just a string, boolean or integer just use
the according data type. More complicated elements, typically those with
attributes and / or sub elements like ``<media:content>`` or
``<media:community>``, (will) have their own classes defined.

Probably you will want to import PyRSS2Gen to make use some of it's helper
classes, e.g. for adding a channel image (``PyRSS2Gen.Image``) or GUIDs to
items (``PyRSS2Gen.Guid``).

Uage is shown by example. For more details check the code and the
`PyRSS2Gen documentation`_.

.. code:: python

    import datetime

    import PyMediaRSS2Gen


    mediaFeed = PyMediaRSS2Gen.MediaRSS2(
        title="A sample Media RSS Feed",
        link="https://github.com/wedi/PyMediaRSS2Gen/",
        description="Description for a feed with media elements"
    )
    mediaFeed.copyright = "Copyright (c) 2014 Foo Inc. All rights reserved."
    mediaFeed.lastBuildDate = datetime.datetime.now()
    mediaFeed.items = [
        PyMediaRSS2Gen.MediaRSSItem(
            title="First item with media element",
            description="An image of foo attached in a media:content element",
            media_content=PyMediaRSS2Gen.MediaContent(
                url="http://example.com/assets/foo1.jpg",
                fileSize=123456,
                medium="image",
                width="480",
                height="640"
            )
        ),
        PyMediaRSS2Gen.MediaRSSItem(
            title="Second item with media element",
            description="A video with multiple resolutions",
            media_content=[
                PyMediaRSS2Gen.MediaContent(
                    url="http://example.com/assets/foo_HD.mp4",
                    fileSize=8765432,
                    type="video/mp4",
                    width="1920",
                    height="1080"
                ),
                PyMediaRSS2Gen.MediaContent(
                    url="http://example.com/assets/foo_SD.mp4",
                    fileSize=2345678,
                    type="video/mp4",
                    width="1280",
                    height="720"
                ),
            ]
        ),
        PyMediaRSS2Gen.MediaRSSItem(
            title="And an item with no media element at all",
            description="An image of foo attached in an media:content element",
            link="http://example.com/article/important-story.html"
        )
    ]
    mediaFeed.write_xml(open("rss2.xml", "w"))



Installation
------------

1. Easiest way to install this module is using pip (as soon as it’s
   uploaded to the PyPI)::

       % pip install PyMediaRSS2Gen

2. If you want to install the module manually, download the package,
   unzip it and run::

       % cd where/you/put/PyMediaRSS2Gen/
       % python setup.py install

   which uses the standard Python installer. `Read the documentation`_ for
   more details about installing Python modules.


How To Contribute
-----------------

Every open source project lives from the generous help by contributors
that sacrifice their time and PyMediaRSS2Gen is no different.

This project lives on `GitHub`_. You are very welcome to fork this
project and submit a pull requests! If you don’t know how to do this
you can still report errors by `opening an issue`_.

Look here for more details about `contributing to PyMediaRSS2Gen`_.


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
.. _PyRSS2Gen documentation: https://pypi.python.org/pypi/PyRSS2Gen/
.. _Read the documentaion: https://docs.python.org/install/index.html
.. _pet project on GitHub: https://github.com/wedi/PyMediaRSS2Gen
.. _open an issue: https://github.com/wedi/PyMediaRSS2Gen/issues
.. _Read the documentation: https://docs.python.org/install/
.. _GitHub: https://github.com/wedi/PyMediaRSS2Gen/
.. _contributing to PyMediaRSS2Gen: https://github.com/wedi/PyMediaRSS2Gen/blob/master/CONTRIBUTING.md
.. _opening an issue: https://github.com/wedi/PyMediaRSS2Gen/issues/
.. _MIT license: https://github.com/wedi/PyMediaRSS2Gen/blob/master/LICENSE.txt
