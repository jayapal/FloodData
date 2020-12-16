from django.urls import path, include
from rest_framework import routers

from . import views as analyse_views

urlpatterns = [
    path('flood-detect/', analyse_views.FloodDetectView.as_view()),
]
