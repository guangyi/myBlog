'''
Created on Jan 5, 2014

@author: zhouguangyi2009

this module is to make sure ajango-autoload function well:
ensure the registration of all database indexes specified in my project

This file need to be stored in the same folder as settings.py
'''

from dbindexer import autodiscover
autodiscover()

from myBlog.models import Author, Post
from django.contrib.auth.models import User 
from dbindexer.lookups import StandardLookup
from dbindexer.api import register_index

register_index(Post,{'author__username': StandardLookup(),})