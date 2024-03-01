from django.db import models
from django_quill.fields import QuillField
from apps.sitewide.models import CommonMain

class Topic(CommonMain):
    THEME = (
        (0,"Select a Theme"),
        (1,"Struggle for Freedom"),
        (2,"A Slave Economy"),
        (3,"The Variety of Enlaved Experience (draft)"),
        (4,"Control and Resistance"),
        (5,"Revolutionary Ideals and Liberty"),
        (6,"Holding On to Humanity"),
        (7,"Myths and Assumptions")
    )    
    theme = models.IntegerField(default=0, choices=THEME)
    has_video = models.BooleanField(default=False)

class Related(models.Model):
    # CASCADE - if parent is deleted, delete the relateds
    topic = models.ForeignKey('Topic', related_name='relateds',
                on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=32)