from django.db import models
from django.utils.translation import ugettext_lazy as _
from post.models import Post

# Create your models here.

class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=30, unique=True)
    posts = models.ManyToManyField(Post, related_name='category')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name