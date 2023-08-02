from django.contrib import admin
from django.urls import path
from . import views

app_name="sitewide"

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    # path("person-model", views.PersonDetailView.as_view(), name="person-model"),
]
