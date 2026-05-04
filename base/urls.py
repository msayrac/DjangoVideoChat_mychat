
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('room/', views.room, name='room'),
    path('get_token/', views.getToken, name='get_token'),
    path('create_member/', views.createMember, name='create_member'),

]

