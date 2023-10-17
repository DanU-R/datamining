from django.urls import path
from clustering_app import views

urlpatterns = [
    path('segmentation/', views.clustering_app, name='clustering_app'),
]
