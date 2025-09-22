from django.urls import path
from . import views

urlpatterns = [
    # Path for your blog's homepage
    path('', views.post_list, name='post_list'),
    
    # Path for individual blog posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]