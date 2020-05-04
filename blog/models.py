from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Blog(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(
        max_length=1000, help_text='Enter a content of the blog')

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse("blog-detail", args=[str(self.id)])

    def __str__(self):
        return self.title


class Blogger(models.Model):

    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(max_length=1000)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse("blogger-detail", args=[str(self.id)])

    def __str__(self):
        return self.name.username


class Comment(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=100, help_text='Enter comment about blog here')
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.description
