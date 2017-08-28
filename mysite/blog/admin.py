from django.contrib import admin
from .models import GuestUser, Post, Comment, Like, CommentAdmin, PostAdmin, LikeAdmin


# Register your models here.
admin.site.register(GuestUser)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
