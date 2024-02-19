from django.db import models
from django_quill.fields import QuillField
from apps.sitewide.models import CommonMain

class EvidenceItem(CommonMain):
    ITEM_TYPE = (
        ('manuscript','Manuscripts'),
        ('printed','Printed material'),
        ('object','Objects'),
        ('picture','Pictures and Paintings')
    )
    item_type = models.CharField(default='select',
        max_length=12, choices=ITEM_TYPE)
    year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField('End, if range', blank=True, null=True)
    is_circa = models.BooleanField(default=False)
    source = models.CharField(max_length=128, blank=True, default='')
    caption = models.TextField(blank=True, default='')
    citation = models.CharField(max_length=128, blank=True, default='')
    accession_num = models.CharField(max_length=32, blank=True, default='')

class Related(models.Model):
    # CASCADE - if parent is deleted, delete the relateds
    evidence_item = models.ForeignKey('EvidenceItem', related_name='relateds',
                on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=32)