from django.conf.urls import url
from Crawler import  views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]