from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Person

class PersonListView(ListView):
    model = Person
    # context_object_name = 'object_list'
    # template_name = 'person/person_list.html' 

class PersonDetailView(TemplateView):
    template_name = "people/person-model.html"