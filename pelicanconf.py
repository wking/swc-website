#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"the Software Carpentry contributors"
SITENAME = u"Software Carpentry"
SITEURL = 'http://software-carpentry.org'

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
DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = False
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

DIRECT_TEMPLATES = [
    'index',
    'archives',
    'authors',
    'categories',
    'tags',
    ]

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
