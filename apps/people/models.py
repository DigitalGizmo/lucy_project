from django.db import models

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
        (0,'entered'),
        (1,'draft'),
        (3,'show')
    )
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, blank=True, default='')
    birth_year = models.IntegerField(blank=True, null=True)
    birth_month = models.IntegerField(blank=True, null=True)
    birth_day = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)
    death_month = models.IntegerField(blank=True, null=True)
    death_day = models.IntegerField(blank=True, null=True)
    gender = models.CharField(default='select', max_length=12, choices=GENDER)
    menu_blurb = models.TextField(blank=True, default='')
    enslavement_status = models.IntegerField(default=0, choices=ENSLAVEMENT_STATUS)
    prod_status = models.IntegerField(default=0, choices=PROD_STATUS)

    def __str__(self):
        return self.first_name + " " + self.last_name