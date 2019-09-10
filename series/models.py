from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

# Create your models here.

class Series(models.Model):
    name = models.CharField(_("Series Name"), max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(_("Slug"))
    
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def no_of_posts(self):
        return self.post_set.count()