from django.shortcuts import render,redirect
from .forms import AlbumForm
from . import models
# Create your views here.

def add_albums(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = AlbumForm()
    return render(request, 'album/add_album.html', {'form': form})


def edit_albums(request , id):
    album = models.Album.objects.get(pk=id)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST , instance=album)
        if form.is_valid():
            form.save()
            return redirect('Home')
    return render(request, 'album/add_album.html', {'form': form})

def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('Home')
