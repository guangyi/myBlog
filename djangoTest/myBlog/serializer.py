'''
Created on Dec 4, 2013

@author: zhouguangyi2009
'''
from rest_framework import serializers
from models import Post, Author
from django.contrib.auth.models import User

class authorSerializer(serializers.ModelSerializer):
    # URL looks like: user/bob/posts
    #posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        #field = ('username', 'email')
    def get_user_url(self, obj):
        return '#/user/%s/' % obj.username  
    user_url = serializers.SerializerMethodField('get_user_url')  

class postSerializer(serializers.ModelSerializer):
    #it will appear in the filed
    #in this case, author returns an Author instance,
    #so angular can call author.name and author.email to get data
    #author = serializers.Field(source="author.username")
    #authorEmail = serializers.Field(source="author.email")
    post_url = serializers.SerializerMethodField('get_post_url')
    class Meta:
        model = Post
        field = ('id','created_on','title','description','post_url','author')
        read_only_fields = ('id', 'created_on')
    #obj??why work    
    def get_post_url(self, obj):
        return '#/post/%s' % obj.id 
    '''def get_validation_exclusions(self):
        # Need to exclude `author` since we'll add that later based off the request
        exclusions = super(postSerializer, self).get_validation_exclusions()
        return exclusions + ['author']'''
class postDetailSerializer(postSerializer):
    author = authorSerializer(required=False)
class userPostSerializer(authorSerializer): 
    posts = postSerializer(many=True)