from django.db import models
# Create your models here.
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField

# Create your models here.
class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    #auther = EmbeddedModelField('Author')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = self.title
        super(Post, self).save(*args, **kwargs)

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name