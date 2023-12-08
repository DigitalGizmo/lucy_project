from django.contrib import admin
from django.db import models
from dataclasses import fields
from django.forms import Textarea
from .models import Topic

class TopicAdmin(admin.ModelAdmin):
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

admin.site.register(Topic, TopicAdmin)