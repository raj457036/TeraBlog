from django import template
from markdown import markdown

register = template.Library()


@register.filter
def show_markdown(text):
    extensions = [
        'fenced_code',
    ]
    return markdown(text, extensions=extensions)
