from django.urls import path
from .views import index
from .adapters.controllers.mgadget_controller import create_mgadget


urlpatterns = [
    path('', index, name='index'),
    path('', create_mgadget),
]
