from django.shortcuts import render
#from django.http import HttpResponse
from .models import Song, SortFilter


def index(request):
    return render(request, 'home/index.html')

def all(request):
    context = {
        'songs' : Song.objects.all()
    }
    return render(request, 'songs/all.html', context)
