from django.contrib import admin
from django.urls import path, include
from shop import views

urlpatterns = [
    path('', views.shopHome, name='ShopHome'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),
    path('productview/', views.productview, name='productview'),
    path('cheackout/', views.cheackout, name='cheackout'),
]