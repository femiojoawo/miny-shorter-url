from django.urls import path
from .views import shorturl , reverse_url

urlpatterns = [
    path('', shorturl, name='index-short'),
    path('<str:url>/',reverse_url,name='reverse-page')

]