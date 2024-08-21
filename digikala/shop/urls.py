from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('single/<int:id>', views.single, name='single'),
    path('product/', views.product, name='product'),
]