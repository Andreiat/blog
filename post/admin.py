from django.contrib import admin
from .models import Post, CommentPost

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create', 'moder')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'text', 'created', 'moder')
    
admin.site.register(Post, PostAdmin)
admin.site.register(CommentPost, CommentAdmin)