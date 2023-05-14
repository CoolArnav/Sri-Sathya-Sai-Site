from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('all/', views.all, name="all-songs"),
]