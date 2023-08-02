from django.contrib import admin
from django.urls import path
from . import views

app_name="moments"

urlpatterns = [
    # path("", views.PersonListView.as_view(), name="menu"),
    path("moment-model", views.MomentTemplatelView.as_view(), name="moment-model"),
]
