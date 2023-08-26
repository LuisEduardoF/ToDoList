from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.event_list),
    path('main/add', views.receive_data, name="add"),
    path('main/change', views.change_data, name="change"),
    path('main/delete', views.delete_data, name="delete")
]
