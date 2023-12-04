from django.contrib import admin
from .models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']
    list_display = ('first_name', 'last_name')

    fields = [
        ('slug', 'prod_status'),
        ('first_name','last_name'),
        ('gender', 'enslavement_status'),
        ('birth_year', 'birth_month', 'birth_day'),
        ('death_year', 'death_month', 'death_day'),
        'menu_blurb', 
        'bio'
    ]
    list_display = ('slug', 'first_name', 'last_name', 'birth_year', 'death_year',
        'enslavement_status',)

admin.site.register(Person, PersonAdmin)