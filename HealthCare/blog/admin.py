from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'enabled', 'published')
    ordering = ('-published',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
