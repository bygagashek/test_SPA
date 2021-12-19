from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('filter_table/', filter_table, name='filter_table'),
]