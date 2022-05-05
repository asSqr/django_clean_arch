from django.urls import path
from .adapters.controllers.mgadget_controller import create_mgadget


urlpatterns = [
    path('', create_mgadget),
]
