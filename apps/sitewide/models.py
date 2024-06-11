from django.db import models
from django_quill.fields import QuillField

class CommonMain(models.Model):
    PROD_STATUS = (
        (0,'background'),
        (1,'proto-menu'),
        (2,'proto-detail')
    )    
    slug = models.SlugField(max_length=32, unique=True)
    title = models.CharField(max_length=64)
    menu_blurb = models.TextField(blank=True, default='')
    full_text = QuillField(blank=True, default='')
    notes = models.TextField(blank=True, default='')
    prod_status = models.IntegerField(default=0, choices=PROD_STATUS)
    ordinal = models.IntegerField(default=99)
    
    class Meta:
        abstract = True


class CommonRelated(models.Model):
    CONTENT_TYPE = (
        ('select','please select'),
        ('evidence','evidence'),
        ('maps','maps'),
        ('people','people'),
        ('topics', 'topics')
    )
    title = models.CharField(max_length=64)
    link = models.CharField(blank=True, null=True, max_length=32)
    content_type = models.CharField(default='select', 
        max_length=12, choices=CONTENT_TYPE)
    slug = models.CharField(blank=True, default='', max_length=32)

    class Meta:
        abstract = True

