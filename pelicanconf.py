#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os as _os
import sys as _sys

_this_dir = _os.path.dirname(__file__)
_sys.path.insert(0, _this_dir)

import pelican_plugins.bootcamp_meta as _bootcamp_meta


PLUGINS = [_bootcamp_meta]


AUTHOR = u"the Software Carpentry contributors"
SITENAME = u"Software Carpentry"
SITEURL = 'http://software-carpentry.org'
CONTACT_EMAIL = 'info@software-carpentry.org'
TWITTER_USERNAME = '@swcarpentry'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

THEME = 'theme/'
JINJA_TRIM_BLOCKS = False
DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = False
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

DIRECT_TEMPLATES = [
    'authors',
    'tags',
    'bootcamps.ics',
    ]

STATIC_PATHS = [
    '3_0',
    '4_0',
    'badges/creator',
    'badges/instructor',
    'badges/organizer',
    'files',
    'img',
    ]

TEMPLATE_PAGE_PATHS = [
    'index.html',
    'about',
    'badges/index.html',
    'badges/creator.html',
    'badges/instructor.html',
    'badges/organizer.html',
    'bootcamps/index.html',
    'bootcamps/conduct.html',
    'blog/index.html',
    'blog/by-date.html',
    'content',
    'license.html',
    'setup',
    ]

ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{directory}/{slug}/'
PAGE_SAVE_AS = '{directory}/{slug}/index.html'
