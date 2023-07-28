from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def asset_path():
    return getattr(settings, "ASSET_PATH", "")