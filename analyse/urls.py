from django.urls import path, include
from rest_framework import routers

from . import views as analyse_views

urlpatterns = [
    path('flood-zones/', analyse_views.FloodZoneView.as_view()),
    path('county-list/', analyse_views.CountyListView.as_view()),
]
