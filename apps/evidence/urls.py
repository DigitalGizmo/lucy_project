from django.urls import path, include
from rest_framework import routers
from . import views

app_name="evidence"

router = routers.DefaultRouter()
router.register(r'api', views.EvidenceItemViewSet)

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls