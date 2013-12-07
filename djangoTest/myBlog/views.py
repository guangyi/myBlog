# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from models import Post
import json
from django.core import serializers
from serializer import postSerializer

def createPost(request):
    #post = json.loads(request.raw_post_data)
    '''Post(
         title = post['title'],
         description = post['description']
         ).save()'''
    posts = serializers.serialize('json', Post.objects.all()) 
    return HttpResponse('posts')

class myPostList(generics.ListCreateAPIView):
    model = Post
    serializer_class = postSerializer
   # template_name = 'myBlog/post_list.html'
     