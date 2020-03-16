from django.contrib import admin

from post.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'title', 'content', 'created', 'draft',
    ]


admin.site.register(Post, PostAdmin)
