from django.urls import path
from .views import home, savol, kurs

urlpatterns = [
    path('', home, name='home'),
    path('savol/', savol, name='savol'),
    path('kurs/', kurs, name='kurs'),
]
