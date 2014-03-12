# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import permissions
from djangoTest.myBlog.models import Post, Author
from serializer import postSerializer, authorSerializer,userPostSerializer,postDetailSerializer
from permissions import isOwnerOrReadOnly
from django.contrib.auth.models import User
'''
def createPost(request):
    #post = json.loads(request.raw_post_data)'''
'''Post(
         title = post['title'],
         description = post['description']
         ).save()
    posts = serializers.serialize('json', Post.objects.all()) 
    return HttpResponse('posts')
'''
class postList(generics.ListCreateAPIView):
    model = Post
    serializer_class = postDetailSerializer
    #comma!!!
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly)  
    def pre_save(self, obj):
        print self.request.user
        obj.author = self.request.user

class postDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Post    
    serializer_class = postDetailSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly)

class userList(generics.ListAPIView):
    #use Author model here
    #use User model only for login
    model = User 
    #queryset = User.objects.all()
    serializer_class = authorSerializer
    #def get_queryset(self):
     #   return Author.objects.all()
    #lookup_filed = 'username'
   # def get_queryset(self):
    #    User.objects.raw_query()
    
class userPostList(generics.ListCreateAPIView):
    model = User
    serializer_class = userPostSerializer
    # filtering against URL like user/bob/posts
    def get_queryset(self):
        #get user name from URL 'name' group
        username = self.kwargs['name']
        #queryset = super(userPostList, self).get_queryset()
        print User.objects.filter(username=username)
        #raw_query is a method provided by mongo_django_engine
        #it's like a filter, only filter out certain author's posts
        return User.objects.filter(username=username)
class singelUserlist(userList):
    def get_queryset(self):
        username = self.kwargs['name']
        return User.objects.filter(username = username)
#class createUser():
'''
class userPostDetail(generics.ListAPIView):
    model = Post
    serializer_class = postSerializer
    def get_queryset(self):
        username = self.kwargs['name']
        pk = self.kwargs['pk']
        return Post.objects.filter(user__name=username)
'''
        