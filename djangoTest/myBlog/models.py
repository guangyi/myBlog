from django.db import models
# Create your models here.
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField
from django_mongodb_engine.contrib import MongoDBManager
from django.contrib.auth.models import User

class Author(models.Model):
    #user = EmbeddedModelField(User)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    #first_name = models.CharField(max_length=30)
    objects = MongoDBManager()   
    def __unicode__(self):
        return self.username
# Create your models here.
class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    #if use id as foreignKey, then in the userPostList
    #it needs index to filter out related posts
    author = models.ForeignKey(User, related_name='posts')
    # mongo-django engine
    # use mongoDBManager then we can call method .raw_query() in views.
    objects = MongoDBManager()   
    def __unicode__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.description:
            self.description = self.title
        super(Post, self).save(*args, **kwargs)


      
#class User(models.User):'''