from django import template
from django.conf import settings

register = template.Library()


@register.filter
def conf(key):
    return settings.CONFIG.get(key, None)
