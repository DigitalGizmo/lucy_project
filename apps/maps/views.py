from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets
from .models import Map
from .serializers import MapSerializer

class MapViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Map.objects.filter(prod_status__gt=0)
    serializer_class = MapSerializer
    lookup_field = 'slug'