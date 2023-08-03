from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
# from .models import 

class MomentTemplatelView(TemplateView):
    template_name = "moments/proof.html"