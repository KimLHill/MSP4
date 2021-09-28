from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<int:gallery_id>/', views.gallery_detail, name='gallery_detail'),
    path('add/', views.add_gallery, name='add_gallery'),
    path('edit/<int:gallery_id>/', views.edit_gallery, name='edit_gallery'),
    path('delete/<int:gallery_id>/', views.delete_gallery, name='delete_gallery'),
]