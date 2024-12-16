from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.inbox, name='inbox'),
    path('send/', views.send_message, name='send_message'),
    path('', views.inbox, name='messages'),
]
