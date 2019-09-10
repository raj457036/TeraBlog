from django.db import models
from mdeditor.fields import MDTextField as MarkDownEditor
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from series.models import Series
from django.conf import settings

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(_("Title"), max_length=255)
    sub_title = models.CharField(_("Sub Title"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    published_on = models.DateTimeField(_("Published On"))
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    content = MarkDownEditor()
    draft = models.BooleanField(_("Is Draft"), default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    