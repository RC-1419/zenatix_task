from . import views
from django.urls import path

urlpatterns = [
    path('login_register', views.login_register),
    path('available_products', views.available_products),
    path('placeAnOrderAndGetBill', views.placeAnOrderAndGetBill),
    path('order_history', views.order_history),
]
