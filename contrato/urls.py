from django.urls import path

from . import views

urlpatterns = [
    path('genera_contrato', views.genera_contrato, name='genera_contrato'),
]