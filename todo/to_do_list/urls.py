from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.event_list, name='main'),
]
