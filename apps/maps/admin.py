from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import Map

class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            ('title', 'slug'),
            'menu_blurb', 
            'full_text', 'notes'
            ]}
        ),
        ('Behind the scenes', {'fields': ['prod_status'],
            'classes': ['collapse']}
        )

    ]
    list_display = ('slug', 'title', 'menu_blurb')
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

admin.site.register(Map, MapAdmin)