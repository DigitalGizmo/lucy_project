from django.db import models
from django_quill.fields import QuillField
from apps.sitewide.models import CommonMain

class Map(CommonMain):
    """
    common fields only
    """

class Related(models.Model):
    # CASCADE - if parent is deleted, delete the relateds
    map = models.ForeignKey('Map', related_name='relateds',
                on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=32)