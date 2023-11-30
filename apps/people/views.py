from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

class PersonListView(ListView):
    model = Person
    # context_object_name = 'object_list'
    # template_name = 'person/person_list.html' 

class PersonDetailView(TemplateView):
    template_name = "people/person-model.html"

class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all().order_by('last_name')
    serializer_class = PersonSerializer