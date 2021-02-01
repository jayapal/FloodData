from django.urls import path, include
from rest_framework import routers

from . import views as oppurtunity_views

urlpatterns = [
    path('opportunity-zone/', oppurtunity_views.OpportunityZoneView.as_view()),

]
