from django.urls import path

from . import views

urlpatterns = [
    path('rezume', views.rezume, name='rezume'),
]

