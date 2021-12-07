from django.contrib import admin
from profiles.models import Comment, Profile, Post, Like, Comment

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
