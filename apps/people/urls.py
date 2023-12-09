# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

app_name="people"

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)

urlpatterns = [
    # path("", views.PersonListView.as_view(), name="menu"),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path("person-model", views.PersonDetailView.as_view(), name="person-model"),
    # path('related/', views.RelatedViewSet.as_view(), name='related')
]

urlpatterns += router.urls