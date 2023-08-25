from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main/', views.event_list, name='main'),
    path('add/', views.EventCreateView.as_view(), name='event_add'),
]
