from django.contrib import admin
from django.urls import path
from . import views

app_name="moments"

urlpatterns = [
    path("", views.MomentListView.as_view(), name="menu"),
    path("community-title", views.MomentTitlelView.as_view(), name="community_title"),
    path("proof", views.MomentTemplatelView.as_view(), name="proof"),
]
