from django.urls import path, include
from rest_framework import routers
from . import views

app_name="myths"

router = routers.DefaultRouter()
router.register(r'api', views.MythViewSet)

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls