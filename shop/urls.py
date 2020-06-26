from django.contrib import admin
from django.urls import path, include, re_path
from shop import views

urlpatterns = [
    path('', views.shopHome, name='ShopHome'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('cart/', views.cart, name='cart'),
    path('placeorder/', views.placeOrder, name='placeOrder'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),
    path('productview/<int:id>', views.productview, name='productview'),
    path('product-view/', views.product_view, name='product_view'),
    # re_path(r'^product-view/(?P<username>\w{0,50})/$', views.product_view, name='product_view'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('cheackout/', views.cheackout, name='cheackout'),
    # path('sentemail/', views.sentemail, name='sentemail'),
    path('man/', views.man, name='man'),
    path('woman/', views.woman, name='woman'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('gen_pdf/', views.gen_pdf, name='gen_pdf'),
]