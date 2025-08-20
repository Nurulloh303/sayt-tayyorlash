



from django.urls import path
from .views import home, brand

urlpatterns = [
    path('', home, name='home'),
    path('brand/', brand, name='brand'),
]
