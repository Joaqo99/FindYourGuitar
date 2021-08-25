from django.urls import path
from . import views

urlpatterns = [
path('', views.mylists, name="mylists"),
]