#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adrián Martínez'
SITENAME = 'Adrián Martínez'
# SITESUBTITLE = 'Mis apuntes y hojas trampa'
THEME = "pujangga"

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'es': '%A, %d de %B del %Y',
    'jp': '%Y-%m-%d(%a)',
}

GITHUB_URL = 'http://github.com/nbicalcarata/'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

SHOW_CONTENT_SUMMARY_ON_INDEX = True
SUMMARY_MAX_LENGTH = 0

LOCALE = 'es_MX.utf8'

DEFAULT_DATE_FORMAT = {'%A %d %B %Y'}
PATH = 'content'
TIMEZONE = 'America/Monterrey'
DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/nbicalcarata'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
PLUGINS = [
    'pelican_gist',
]