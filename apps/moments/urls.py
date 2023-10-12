from django.contrib import admin
from django.urls import path
from . import views

app_name="moments"

urlpatterns = [
    path("", views.MomentListView.as_view(), name="menu"),
    path("community", views.MomentTitlelView.as_view(), name="community"),
    path("community-scroll", views.MomentTemplatelView.as_view(), name="community_scroll"),
    path("community-scroll-model", views.MomentModelTemplatelView.as_view(), name="community_scroll_model"),
    path("community-frames", views.FrameJsonView, name="community-frames")
]
