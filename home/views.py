from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Song, SortFilter
from django.contrib import messages


def index(request):
    return render(request, 'home/index.html')


def all(request):
    context = {
        'songs' : Song.objects.all()
    }
    return render(request, 'songs/all.html', context)



class SongListView(ListView):
    model = Song
    template_name = 'songs/all.html'
    context_object_name = 'songs'


class SongDetailView(DetailView):
    model = Song
    template_name = 'songs/song-detail.html'


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        songs = Song.objects.none()
    else:
        songsTitle = Song.objects.filter(name__icontains=query)
        songsDescription = Song.objects.filter(description__icontains=query)
        songsGod = Song.objects.filter(god__name__icontains=query)
        songsRaga = Song.objects.filter(Raaga__name__icontains=query)
        songs = songsTitle.union(songsDescription, songsGod, songsRaga)

    if songs.count() == 0:
        messages.error(request, "No search results found. Please refine your query.", extra_tags="danger")

    context = {
        'songs': songs,
        'query': query,
        }
    return render(request, 'songs/search.html', context)

