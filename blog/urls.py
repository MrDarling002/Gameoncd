from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('category/<slug:slug>/',views.category,name = 'category'),
    path('search/', views.search_function, name='search'),
    path('posts/<slug:slug>', views.post_detail, name='post_detail_url'),
    path('posts/<slug:slug>/comment/', views.comment, name='comment'),
    path('register/', views.register, name='register'),
    path('game_dev/',views.game_dev,name = 'game_dev'),
    path('game_dev/<slug:slug>',views.game_category,name = 'game_category'),
    path('game_category/<slug:slug>', views.game_post, name='game_post'),
    path('game_post/<slug:slug>', views.game, name='game_url'),
    path('game_text/',views.game_text,name = 'game_text'),


]
