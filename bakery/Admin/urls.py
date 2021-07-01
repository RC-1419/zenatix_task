from . import views
from django.urls import path

urlpatterns = [
    path('add_ingredients', views.add_ingredients),
    path('createBakeryItem', views.createBakeryItem),
    path('detailOfBakeryItem', views.detailOfBakeryItem),
    path('manageInventory', views.manageInventory),
]
