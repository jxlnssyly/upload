from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()

@register.filter
def imageUrl(value):
    return value.images.first().image.url

@register.filter
def typeFilter(value):
    if value == '1,':
        return "photography"
    if value == '2,':
        return "design"
    if value == '3,':
        return 'diary'
    return ""
