from django.urls import path
from . import views

app_name="Products"

urlpatterns=[
    path('', views.Home, name="home"),
    path('<slug:slug>', views.ProductDetail, name="Detail"),
    path('<slug:slug>/order/', views.Order, name="Order"),
    path('<slug:slug>/order/check-out', views.checkOut, name="checkout"),
   path('cart/', views.Cart, name="cart"),
]


