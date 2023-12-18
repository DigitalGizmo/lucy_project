from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets
from .models import EvidenceItem
from .serializers import EvidenceItemSerializer

class EvidenceItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EvidenceItem.objects.filter(prod_status__gt=0)
    serializer_class = EvidenceItemSerializer
    lookup_field = 'slug'