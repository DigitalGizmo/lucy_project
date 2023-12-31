from django.db import models
from django_quill.fields import QuillField

class Myth(models.Model):
    PROD_STATUS = (
        (0,'hide'),
        (1,'show'),
        (2,'active')
    )    
    slug = models.SlugField(max_length=32, unique=True)
    title = models.CharField(max_length=64)
    menu_blurb = models.TextField(blank=True, default='')
    full_text = QuillField(blank=True, default='')
    notes = models.TextField(blank=True, default='')
    prod_status = models.IntegerField(default=1, choices=PROD_STATUS)
   
