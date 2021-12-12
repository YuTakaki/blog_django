from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=False, default=None, on_delete= models.CASCADE)
    slug = models.CharField(default="", max_length=10)
    def __str__(self):
        return self.title
    def bodySnippet(self):
        return self.body[:50] + "..."