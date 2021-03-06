from django.contrib import admin
from django.urls import path
from app import views


app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('add_album/', views.album_form, name='album_form'),
    path('add_musician/', views.musician_form, name='musician_form'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_artist/<int:artist_id>/', views.delete_musician, name='delete_artist'),


]