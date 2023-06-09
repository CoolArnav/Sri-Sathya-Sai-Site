from django.urls import path
from . import views
from .views import SongListView, SongDetailView

urlpatterns = [
    path('', views.index, name="home"),
    path('song/all/', SongListView.as_view(), name="all-songs"),
    path('song/<int:pk>/', SongDetailView.as_view(), name="song-detail"),
    #path('user/favourite/(?P<id>\d+)/', views.favourite_post, name="favourite-post"),
    path('search/', views.search, name="search"),
]