# coding=utf-8
"""PyMediaRSS2Gen - A Python library for generating Media RSS 2.0 feeds.

http://www.rssboard.org/media-rss
"""

from __future__ import absolute_import
from __future__ import unicode_literals

__name__ = "PyMediaRSS2Gen"
__version__ = '0.0.1'
__author__ = 'Dirk Weise <code@dirk-weise.de>'

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import PyRSS2Gen

_generator_name = __name__ + " " + __version__
_media_elements = ['media_rating', 'media_title', 'media_description',
                   'media_keywords', 'media_thumbnail', 'media_category',
                   'media_hash', 'media_credit', 'media_copyright',
                   'media_text', 'media_restriction', 'media_community',
                   'media_comments', 'media_embed', 'media_responses',
                   'media_backLinks', 'media_status', 'media_price',
                   'media_license', 'media_subTitle', 'media_rights',
                   'media_scenes']


class MediaRSS2(PyRSS2Gen.RSS2, object):

    """The main class representing a Media RSS Feed."""

    def to_xml(self, encoding="UTF-8"):
        """Return the Media RSS Feed's XML representation."""
        # we add the media namespace if we see any media items
        if any([key for item in self.items
                for key in vars(item)
                if key.startswith('media_') and getattr(item, key)]):
            self.rss_attrs["xmlns:media"] = "http://search.yahoo.com/mrss/"
        self.generator = _generator_name
        return super(MediaRSS2, self).to_xml(encoding)

    def write_xml(self, outfile, encoding="UTF-8"):
        """Write the Media RSS Feed's XML representation to the given file."""
        # we add the media namespace if we see any media items
        if any([key for item in self.items for key in vars(item) if
                key.startswith('media_') and getattr(item, key)]):
            self.rss_attrs["xmlns:media"] = "http://search.yahoo.com/mrss/"
        self.generator = _generator_name
        super(MediaRSS2, self).write_xml(outfile, encoding)


class MediaContent(object):

    """Publish a media:content element."""

    element_attrs = None

    def __init__(
        self,
        url=None,
        fileSize=None,
        type=None,
        medium=None,
        isDefault=None,
        expression=None,
        bitrate=None,
        framerate=None,
        samplingrate=None,
        channels=None,
        duration=None,
        height=None,
        width=None,
        lang=None
    ):
        """Create a media:content element, args will be attributes."""
        self.element_attrs = OrderedDict()

        self._add_attribute('url', url)
        self._add_attribute('fileSize', fileSize)
        self._add_attribute('type', type)
        self._add_attribute('medium', medium,
                            ['image', 'audio', 'video', 'document',
                             'executable'])
        self._add_attribute('isDefault', isDefault, ['true', 'false'])
        self._add_attribute('expression', expression,
                            ['sample', 'full', 'nonstop'])
        self._add_attribute('bitrate', bitrate)
        self._add_attribute('framerate', framerate)
        self._add_attribute('samplingrate', samplingrate)
        self._add_attribute('channels', channels)
        self._add_attribute('duration', duration)
        self._add_attribute('height', height)
        self._add_attribute('width', width)
        self._add_attribute('lang', lang)

    def _add_attribute(self, name, value, allowed_values=None):
        """Add an attribute to the MediaContent element."""
        if value and value != 'none':

            if isinstance(value, (int, bool)):
                value = str(value)

            if allowed_values and value not in allowed_values:
                raise TypeError(
                    "Attribute '" + name + "' must be one of " + str(
                        allowed_values) + " but is '" + str(value) + "'")

            self.element_attrs[name] = value

    def publish(self, handler):
        """Publish the MediaContent as XML."""
        PyRSS2Gen._element(handler, "media:content", None, self.element_attrs)

    def __repr__(self):
        """Return a nice string representation for prettier debugging."""
        return "MediaContent(url='%s', type='%s', width='%s', height='%s')" % \
               (self.element_attrs.get('url', None),
                self.element_attrs.get('type', None),
                self.element_attrs.get('height', None),
                self.element_attrs.get('width', None))


class MediaRSSItem(PyRSS2Gen.RSSItem, object):

    """Publish a Media RSS Item."""

    def __init__(
        self,

        title=None,  # string
        description=None,  # string
        link=None,  # url as string
        guid=None,  # unique string (e.g. url)

        media_group=None,
        # Allows grouping of <media:content> elements with the same content.
        media_content=None,  # can be used to publish any type of media.
        media_player=None,
        # Allows a media object to be accessed through a web browser media
        # player console.
        media_peerLink=None,  # P2P link.
        media_location=None,
        # element to specify geographical information . The format conforms
        # to geoRSS.

        **kwargs
    ):
        """Create a Media RSS item that contains args as elements."""
        self.media_group = media_group
        self.media_content = media_content
        self.media_player = media_player
        self.media_peerLink = media_peerLink
        self.media_location = media_location
        [setattr(self, key, kwargs.pop(key)) for key in _media_elements if
         key in kwargs]

        # call base class constructor, attach all left over arguments
        super(MediaRSSItem, self).__init__(
            title=title,
            link=link,
            description=description,
            guid=guid,
            **kwargs
        )

        self.check_complicance()

    def __repr__(self):
        """Return a nice string representation for prettier debugging."""
        return "MediaContent(title='%s', media_content='%s', " \
               "media_group='%s', media_player='%s', media_peerLink='%s', " \
               "media_location='%s')" % (
                   self.title,
                   str(self.media_content),
                   str(self.media_group),
                   str(self.media_player),
                   str(self.media_peerLink),
                   str(self.media_location)
               )

    def check_complicance(self):
        """Check compliance with Media RSS Specification, Version 1.5.1.

        see http://www.rssboard.org/media-rss
        Raises AttributeError on error.
        """
        # check Media RSS requirement: one of the following elements is
        # required: media_group | media_content | media_player | media_peerLink
        # | media_location. We do the check only if any media_... element is
        # set to allow non media feeds
        if(any([ma for ma in vars(self)
                if ma.startswith('media_') and getattr(self, ma)])
           and not self.media_group
           and not self.media_content
           and not self.media_player
           and not self.media_peerLink
           and not self.media_location
           ):
            raise TypeError(
                "Using media elements requires the specification of at least "
                "one of the following elements: 'media_group', "
                "'media_content', 'media_player', 'media_peerLink' or "
                "'media_location'.")

        # check Media RSS requirement: if media:player is missing all
        # media_content elements need to have url attributes.
        if not self.media_player:
            if self.media_content:
                # check if all media_content elements have a URL set
                if isinstance(self.media_content, list):
                    if not all([False for mc in self.media_content if
                                'url' not in mc.element_attrs]):
                        raise AttributeError(
                            "MediaRSSItems require a media_player attribute "
                            "if a media_content has no url set.")
                else:
                    if not self.media_content.element_attrs['url']:
                        raise AttributeError(
                            "MediaRSSItems require a media_player attribute "
                            "if a media_content has no url set.")
                pass
            elif self.media_group:
                # check media groups without player if its media_content
                # elements have a URL set
                raise NotImplementedError(
                    "MediaRSSItem: media_group check not implemented yet.")

    def publish_extensions(self, handler):
        """Publish the Media RSS Feed elements as XML."""
        if isinstance(self.media_content, list):
            [PyRSS2Gen._opt_element(handler, "media:content", mc_element) for
             mc_element in self.media_content]
        else:
            PyRSS2Gen._opt_element(handler, "media:content",
                                   self.media_content)

        if hasattr(self, 'media_title'):
            PyRSS2Gen._opt_element(handler, "media:title", self.media_title)

        if hasattr(self, 'media_text'):
            PyRSS2Gen._opt_element(handler, "media:text", self.media_text)
