
from django.shortcuts import render
from album.models import Album

def home(request):
    datas = Album.objects.all()
    return render(request, 'home.html', {'datas': datas})