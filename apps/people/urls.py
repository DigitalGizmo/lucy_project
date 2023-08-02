from django.contrib import admin
from django.urls import path
from . import views

app_name="people"

urlpatterns = [
    path("", views.PersonListView.as_view(), name="menu"),
    path("person-model", views.PersonDetailView.as_view(), name="person-model"),
]
