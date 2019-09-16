from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_link, name='get_link')
]