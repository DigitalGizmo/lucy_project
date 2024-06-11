from django.db import models
from django_quill.fields import QuillField
from apps.sitewide.models import CommonMain, CommonRelated

class Map(CommonMain):
    """
    common fields only
    """
    class Meta:
        ordering = ['title']

class Related(CommonRelated):
    # CASCADE - if parent is deleted, delete the relateds
    map = models.ForeignKey('Map', related_name='relateds',
                on_delete=models.CASCADE)
