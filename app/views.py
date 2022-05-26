from django.shortcuts import render
from django.http import HttpResponse
from app.models import Musician, Album
from app import forms

# Create your views here.


def index(request):
    musician_list = Musician.objects.order_by("first_name")
    diction = {"title": "Home Page", 'musician_list': musician_list}
    return render(request, 'app/index.html', context=diction)


def album_list(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list1 = Album.objects.filter(artist=artist_id)

    diction = {'title': 'List of Albums', 'artist_info': artist_info, 'album_list1': album_list1}
    return render(request, 'app/album_list.html', context=diction)


def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title': 'Add Musician', 'musician_form':form}
    return render(request, 'app/form.html', context=diction)


def album_form(request):
    form = forms.AlbumForm()

    if request.method == "POST":
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction ={'title': ' Add Album', 'album_form': form}
    return render(request, 'app/album_form.html', context=diction)


def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST,instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request,artist_id)

    diction = {'edit_form':form}
    return render(request, 'app/edit_artist.html', context=diction)


def edit_album(request, album_id):
    album_info = Album.objects.get(pk=1)
    form = forms.AlbumForm(instance=album_info)
    dicstion = {}
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            dicstion.update({'success_text':'Successfully Updated'})

    dicstion.update({'edit_form':form})
    dicstion.update({'album_id':album_id})
    return render(request, 'app/edit_album.html', context=dicstion)


def delete_album(request,album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction= {'delete_Successfully': "Delete Successfully!"}
    return render(request, 'app/delete.html', context=diction)


def delete_musician(request,artist_id):
    artist = Musician.objects.get(pk=artist_id).delete(0)
    diction = {'delete_Successfully': "Delete Successfully!"}
    return render(request, 'app/delete.html', context=diction)