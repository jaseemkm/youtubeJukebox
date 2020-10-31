from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^vote/$', views.vote, name='vote'),
    url(r'logout', views.logout, name='logout'),
]
