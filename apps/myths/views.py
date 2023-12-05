from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets
from .models import Myth
from .serializers import MythSerializer

class MythViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Myth.objects.all()
    serializer_class = MythSerializer
    lookup_field = 'slug'