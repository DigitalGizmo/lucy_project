from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
# from .models import 

class EvidenceListView(TemplateView):
    # model = Moment
    # context_object_name = 'object_list'
    template_name = 'evidence/evidence_list.html'

# class MomentTitlelView(TemplateView):
#     template_name = "moments/moment_title.html"

# class MomentTemplatelView(TemplateView):
#     template_name = "moments/proof.html"