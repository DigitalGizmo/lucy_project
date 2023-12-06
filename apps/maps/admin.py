from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import Map

class MapAdmin(admin.ModelAdmin):
    fields = [
        ('slug', 'prod_status'),
        'title',
        'menu_blurb', 
        'full_text', 'notes'
    ]
    list_display = ('slug', 'title', 'menu_blurb')
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

admin.site.register(Map, MapAdmin)