from django.urls import path
from imovelApp import views

urlpatterns = [
    path('', views.mysite, name='mysite')
]
