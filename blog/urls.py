from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('search/', views.search_function, name='search'),
    path('posts/<slug:slug>', views.post_detail, name='post_detail_url'),
    path('posts/<slug:slug>/comment/', views.comment, name='comment'),
    path('register/', views.register, name='register'),
]
