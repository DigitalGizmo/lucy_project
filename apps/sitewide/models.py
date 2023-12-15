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
    prod_status = models.IntegerField(default=1, choices=PROD_STATUS)

    class Meta:
        abstract = True
