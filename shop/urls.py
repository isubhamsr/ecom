from django.contrib import admin
from django.urls import path, include, re_path
from shop import views

urlpatterns = [
    path('', views.shopHome, name='ShopHome'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),
    path('productview/<int:id>', views.productview, name='productview'),
    path('product-view/', views.product_view, name='product_view'),
    # re_path(r'^product-view/(?P<username>\w{0,50})/$', views.product_view, name='product_view'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('cheackout/', views.cheackout, name='cheackout'),
]