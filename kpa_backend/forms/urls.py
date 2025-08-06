from django.urls import path
from .views import create_wheel_spec, create_bogie_checksheet

urlpatterns = [
    path('forms/wheel-specifications', create_wheel_spec),
    path('forms/bogie-checksheet', create_bogie_checksheet),
]
