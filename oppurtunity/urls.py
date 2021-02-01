from django.urls import path, include
from rest_framework import routers

from . import views as oppurtunity_views

urlpatterns = [
    path('oppurtunity-zone/', oppurtunity_views.OppurtinityZoneView.as_view()),

]
