from django.urls import path
from .adapters.controllers.mgadget_controller import (
    retrieve_mgadget,
    create_mgadget,
)


urlpatterns = [
    path('<str:id>', retrieve_mgadget),
    path('', create_mgadget),
]
