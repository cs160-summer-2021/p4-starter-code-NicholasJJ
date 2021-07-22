# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('bigDisplay', views.bigDisplay, name='bigDisplay'),
    path('smallDraw', views.smallDraw, name='smallDraw'),
    path('getGroupInfo', views.getGroupInfo, name='getGroupInfo'),
    path('wsp', views.wsp, name='wsp'),
]
