'''
Created on Dec 4, 2013

@author: zhouguangyi2009
'''
from rest_framework import serializers
from models import Post

class postSerializer(serializers.ModelSerializer):
    #it will appear in the filed
    api_url = serializers.SerializerMethodField('get_api_url')
    class Meta:
        model = Post
        field = ('id','title','description','api_url','created_on')
    #obj??why work    
    def get_api_url(self, obj):
        return '#/post/%s' % obj.id 
        