from django.urls import path
from .views import shorturl

urlpatterns = [
    path('', shorturl, name='index-short')
]