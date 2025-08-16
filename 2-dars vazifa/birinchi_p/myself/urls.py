from django.urls import path
from .views import index, contact, instagram

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('instagram/', instagram, name='instagram'),
]
