from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import Person, Related

class RelatedInline(admin.StackedInline):
    model = Related
    extra = 2
    fields = ['person', ('title', 'link')]
    # formfield_overrides = {
    #     # models.CharField: {'widget': TextInput(attrs={'size':'60'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':80})},
    # }

class PersonAdmin(admin.ModelAdmin):
    change_form_template = 'people/admin/quill_override.html'
    fieldsets = [
        (None, {'fields': [
            ('first_name','last_name', 'slug'),
        ('gender', 'enslavement_status'),
        ('birth_year', 'birth_month', 'birth_day'),
        ('death_year', 'death_month', 'death_day'),
        'menu_blurb', 
        'bio', 'notes'
            ]}
        ),
        ('Behind the scenes', {'fields': ['prod_status']})
    ]
    list_display = ('slug', 'first_name', 'last_name', 'birth_year', 'death_year',
        'enslavement_status', 'prod_status')
    list_filter  = ['prod_status']
    search_fields = ['first_name', 'last_name', 'slug']
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }
    inlines = [RelatedInline]

admin.site.register(Person, PersonAdmin)