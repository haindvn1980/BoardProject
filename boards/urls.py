from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from boards import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:boards_id>/', views.board_topics, name='board_topics'),
    path('boards/<int:boards_id>/new/', views.new_topic, name='new_topic'),
]
