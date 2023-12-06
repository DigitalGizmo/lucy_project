from django.db import models
from django_quill.fields import QuillField

class EvidenceItem(models.Model):
    ITEM_TYPE = (
        ('manuscript','Manuscripts'),
        ('printed','Printed material'),
        ('object','Objects'),
        ('picture','Pictures and Paintings')
    )
    PROD_STATUS = (
        (0,'hide'),
        (1,'show'),
        (2,'active')
    )    
    slug = models.SlugField(max_length=32, unique=True)
    title = models.CharField(max_length=64)
    menu_blurb = models.TextField(blank=True, default='')
    full_text = QuillField(blank=True, default='')
    item_type = models.CharField(default='select',
        max_length=12, choices=ITEM_TYPE)
    year = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=128, blank=True, default='')
    citation = models.CharField(max_length=128, blank=True, default='')
    accession_num = models.CharField(max_length=32, blank=True, default='')
    notes = models.TextField(blank=True, default='')
    prod_status = models.IntegerField(default=1, choices=PROD_STATUS)


