from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import EvidenceItem, Related

class RelatedInline(admin.StackedInline):
    model = Related
    extra = 2
    fields = ['evidence_item', ('title', 'link')]

class EvidenceItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            ('title', 'slug'),
            ('item_type', 'accession_num'),
            ('year', 'end_year'),
            'menu_blurb', 
            'full_text', 'caption',
            'source', 'citation','notes'
            ]}
        ),
        ('Behind the scenes', {'fields': ['prod_status']})
    ]
    list_display = ('slug', 'title', 'year', 'menu_blurb')
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }
    inlines = [RelatedInline]

admin.site.register(EvidenceItem, EvidenceItemAdmin)