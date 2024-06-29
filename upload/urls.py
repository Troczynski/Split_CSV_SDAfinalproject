from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('success/', views.success_view, name='success_view'),
    path('invalid_file/', views.invalid_file_view, name='invalid_file_view'),
    path('download/', views.download_file, name='download_file'),
    path('download/<str:filename>/', views.download_single_file, name='download_single_file'),
]
