from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'enabled', 'published')
    ordering = ('-published',)


admin.site.register(Post, PostAdmin)
