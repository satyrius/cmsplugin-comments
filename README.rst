==================
cmsplugin-comments
==================

|ci|

.. |ci| image:: https://travis-ci.org/satyrius/cmsplugin-comments.svg?branch=master
    :target: https://travis-ci.org/satyrius/cmsplugin-comments

Django CMS plugin to add comments for any page

Requirements
============

It works fine and tested under ``Python 2.7``. The following libraries are required

- ``Django`` >= 1.5
- ``django-cms`` >= 3.0 (we recommend to use Django CMS 3.0 and higher, contact us if you need prior CMS versions supports and have some issues)

Installation
============

::

**The plugin is in development and not releasen on pypi, you should install it from repo**

$ pip install -e git+https://github.com/satyrius/cmsplugin-comments.git@master#egg=cmsplugin_comments

Configure installed apps in your ``settings.py`` ::

  INSTALLED_APPS = [
      # django contrib and django cms apps
      'cmsplugin_comments',
  ]

Migrate your database ::

  django-admin.py migrate cmsplugin_comments
