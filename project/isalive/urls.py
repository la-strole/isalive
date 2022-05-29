from django.urls import path
from . import views
urlpatterns = [
    path('', views.is_alive, name='isalive'),
]
