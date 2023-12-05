from django.db import models
from django_quill.fields import QuillField

class Topic(models.Model):
    slug = models.SlugField(max_length=32, unique=True)
    title = models.CharField(max_length=64)
    menu_blurb = models.TextField(blank=True, default='')
    full_text = QuillField(blank=True, default='')
   
