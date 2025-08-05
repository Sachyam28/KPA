from django.urls import path
from .views import create_wheel_spec, create_bogie_checksheet, get_wheel_spec_filtered

urlpatterns = [
    path('forms/wheel-specifications', create_wheel_spec),
    path('forms/bogie-checksheet', create_bogie_checksheet),
    path('forms/wheel-specifications/filter/', get_wheel_spec_filtered),  # for GET with filters
]
