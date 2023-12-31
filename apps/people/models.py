from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Person(models.Model):
    GENDER = (
        ('select','please select'),
        ('male','male'),
        ('female','female'),
        ('unknown', 'unknown'),
    )
    ENSLAVEMENT_STATUS = (
        (0,'please select'),
        (1,'enslaved'),
        (2,'enslaved, then free'),
        (3,'always free'),
        (4,'enslaver'),
        (5,'not enslaver')
    )
    PROD_STATUS = (
        (0,'background'),
        (1,'proto-menu'),
        (2,'proto-detail')
    )
    slug = models.SlugField(max_length=32, unique=True)
    bio = QuillField(blank=True, default='')
    menu_blurb = models.TextField(blank=True, default='')
    notes = models.TextField(blank=True, default='')
    prod_status = models.IntegerField(default=0, choices=PROD_STATUS)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, blank=True, default='')
    birth_year = models.IntegerField(blank=True, null=True)
    birth_month = models.IntegerField(blank=True, null=True)
    birth_day = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)
    death_month = models.IntegerField(blank=True, null=True)
    death_day = models.IntegerField(blank=True, null=True)
    gender = models.CharField(default='select', max_length=12, choices=GENDER)
    fake_related = QuillField(blank=True, default='')
    enslavement_status = models.IntegerField(default=0, choices=ENSLAVEMENT_STATUS)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Related(models.Model):
    # CASCADE - if person is deleted, delete the relateds
    person = models.ForeignKey('Person', related_name='relateds',
                on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=32)