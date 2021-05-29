from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(max_length=250)
    content = models.TextField(default='(empty)')
    published = models.DateField(auto_now_add=True)
    pic = models.ImageField(upload_to='pics', null=True, blank=True, default='default.png')
    enabled = models.BooleanField(default=False)
    tags = TaggableManager()

    class Meta:
        ordering = ['-published']
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
