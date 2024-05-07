from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import Map, Related

class RelatedInline(admin.StackedInline):
    model = Related
    extra = 2
    fields = ['map', ('title', 'content_type', 'slug')]

class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            ('title', 'slug'),
            'menu_blurb', 
            'full_text', 'notes'
            ]}
        ),
        ('Behind the scenes', {'fields': ['prod_status']})

    ]
    list_display = ('slug', 'title', 'menu_blurb')
    list_filter  = ['prod_status'] 
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }
    inlines = [RelatedInline]

admin.site.register(Map, MapAdmin)