from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Nvdemande'),
    path('', views.statistiques, name='statistique'),
    path('envoyer-avec-success/', views.confirmation, name='confirmation'),
    #path('contact', views.ContactDetails),
]
