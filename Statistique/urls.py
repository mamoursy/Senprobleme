from django.urls import path

from . import views

urlpatterns = [
    path('statistiques', views.index, name='statistique'),
    ]
