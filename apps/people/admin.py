from django.contrib import admin
from .models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']
    list_display = ('first_name', 'last_name')

admin.site.register(Person, PersonAdmin)