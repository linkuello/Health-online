from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(max_length=250)
    content = models.TextField(default='(empty)')
    published = models.DateField(auto_now_add=True)
    url = models.URLField(default='', max_length=500)
    enabled = models.BooleanField(default=False)
    tags = TaggableManager()

    def __str__(self):
        return self.title
