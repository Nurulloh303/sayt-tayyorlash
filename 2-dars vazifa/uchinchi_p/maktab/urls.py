from django.urls import path
from .views import sinf, bmw, mers

urlpatterns = [
    path('', sinf, name='sinf'),
    path('bmw/', bmw, name='bmw'),
    path('mers/', mers, name='mers'),
]