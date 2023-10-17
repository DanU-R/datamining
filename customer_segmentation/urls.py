from django.urls import path
from clustering_app import views

urlpatterns = [
    path('', views.index),
    path('segmentation/', views.customer_segmentation, name='clustering_app'),
]
