from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.Home, name='chat_home'),
    path('post/', views.Post, name='chat_post'),
    path('messages/', views.Messages, name='chat_messages'),
]