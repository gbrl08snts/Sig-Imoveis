from django.urls import path
from imovelApp import views

urlpatterns = [
    path('', views.list_location, name='list-location'),
    path('form-client/', views.form_client, name='client-create'),
    path('form-immobile/', views.form_immobile, name='immobile-create'),
    path('form-location/<int:id>/', views.form_location, name='location-create'),
]
