"""Models architecture."""

from django.db import models
from django.contrib import admin
import datetime


# Create your models here.
class GuestUser(models.Model):
    """Guest user table."""

    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    Email = models.EmailField(max_length=254)
    Password = models.CharField(max_length=250)

    def __str__(self):
        """Return string with Email."""
        return self.Email


class Post(models.Model):
    """Post table."""

    PostTitle = models.CharField(max_length=250, verbose_name='Title')
    PostDate = models.DateTimeField(verbose_name='Post Date')
    PostImageURL = models.URLField(max_length=250, verbose_name='Image URL')
    PostText = models.TextField(verbose_name='Post Text')
    GuestUserKey = models.ForeignKey(
        GuestUser, on_delete=models.CASCADE, verbose_name='Guest User')
    PostVisible = models.BooleanField(
        default=False, verbose_name='Post Visible?')

    def __str__(self):
        """Format string and return."""
        template = '{0.PostTitle}'
        return template.format(self)

    def was_published_recently(self):
        """Return newest posts."""
        return self.PostDate >= timezone.now() - datetime.timedelta(days=15)

    def is_post_visible(self):
        """Return only visible posts."""
        return self.PostVisible.order_by('-PostDate')


class PostAdmin(admin.ModelAdmin):
    """Admin Post table."""

    list_display = ('PostTitle', 'PostDate', 'GuestUserKey')
    search_fields = ['PostTitle', 'PostDate']
    list_filter = ('PostTitle', 'PostDate')


class Comment(models.Model):
    """Comments table."""

    CommentText = models.TextField()
    CommentDate = models.DateTimeField(
        auto_now=True, verbose_name='Comment Date')
    GuestUserKey = models.ForeignKey(
        GuestUser, on_delete=models.CASCADE, verbose_name='Guest User')
    PostKey = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Post')

    def __str__(self):
        """Format and return string."""
        template = '{0.PostKey.PostTitle} - {0.GuestUserKey.FirstName}'
        return template.format(self)


class CommentAdmin(admin.ModelAdmin):
    """Admin Comment table."""

    list_display = ('CommentDate', 'GuestUserKey', 'PostKey')


class Like(models.Model):
    """Likes table."""

    LikeDate = models.DateTimeField(auto_now=True, verbose_name='Like Date')
    GuestUserKey = models.ForeignKey(
        GuestUser, on_delete=models.CASCADE, default=1,
        verbose_name='Guest User')
    PostKey = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Post')

    def __str__(self):
        """Format and return string."""
        template = '{0.GuestUserKey.FirstName}'
        return template.format(self)


class LikeAdmin(admin.ModelAdmin):
    """Admin Like table."""

    list_display = ('GuestUserKey', 'LikeDate', 'PostKey')
