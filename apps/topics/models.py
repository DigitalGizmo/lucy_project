from django.db import models
from django_quill.fields import QuillField
from apps.sitewide.models import CommonMain

class Topic(CommonMain):
    THEME = (
        (0,'Myths'),
        (1,'Emancipation'),
        (2,'Another Theme')
    )    
    theme = models.IntegerField(default=0, choices=THEME)

class Related(models.Model):
    # CASCADE - if parent is deleted, delete the relateds
    topic = models.ForeignKey('Topic', related_name='relateds',
                on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=32)