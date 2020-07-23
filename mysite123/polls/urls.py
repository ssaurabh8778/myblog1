from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home/total_filled1', views.total_filled1, name='Total Filled'),
    path('home/data_interface1', views.data_interface1, name='Data Filling Interface'),
    path('home/testing1', views.testing1, name='Data Filling Interface'),
    path('home/testing_data1', views.testing_data1, name='Data Filling Interface'),
]

