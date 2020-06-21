from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    url ('portfolio/', views.portfolio, name='portfolio'),
    url ('contact/', views.contact, name='contact'),
    

]