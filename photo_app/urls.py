from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.gallery, name="gallery"),
    path('photo/<str:pk>/', views.view_photo, name="photo"),
    path('upload_photo/', views.upload_photo, name="upload_photo"),
]
