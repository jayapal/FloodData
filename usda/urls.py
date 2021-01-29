from django.urls import path, include
from rest_framework import routers

from . import views as usda_views

urlpatterns = [
    path('usda-eligibility/', usda_views.UsdaEligibilityView.as_view()),

]
