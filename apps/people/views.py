from django.shortcuts import render
from django.views.generic import TemplateView

class PersonListView(TemplateView):
    template_name = "people/home.html"
