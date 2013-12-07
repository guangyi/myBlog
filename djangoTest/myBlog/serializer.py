'''
Created on Dec 4, 2013

@author: zhouguangyi2009
'''
from rest_framework import serializers
from models import Post

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ('title','description')