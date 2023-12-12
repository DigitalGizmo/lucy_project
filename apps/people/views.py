from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework import viewsets
from .models import Person, Related
from .serializers import PersonSerializer

class PersonListView(ListView):
    model = Person
    # context_object_name = 'object_list'
    # template_name = 'person/person_list.html' 

class PersonDetailView(TemplateView):
    template_name = "people/person-model.html"

class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.filter(prod_status__gt=0).order_by('first_name')
    serializer_class = PersonSerializer
    lookup_field = 'slug'

# temp while figuring related relation
# class RelatedViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Related.objects.all()
#     serializer_class = RelatedSerializer