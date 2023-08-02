from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=32, blank=True, default='')
    last_name = models.CharField(max_length=32, blank=True, default='')

    def __str__(self):
        return self.first_name + " " + self.last_name