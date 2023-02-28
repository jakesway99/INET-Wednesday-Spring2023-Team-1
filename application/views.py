from django.shortcuts import render, HttpResponse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .forms import *


def home(request):
    return HttpResponse("Hello, world. You're at the NYUBeatBuddies application!")


def profile_edit(request):
    client_credentials_manager = SpotifyClientCredentials()

    token_dict = client_credentials_manager.get_access_token()
    token = token_dict["access_token"]
    context = {
        "OAuth": token,
        "song_form": SongEdit(),
        "artist_form": ArtistEdit(),
        "album_form": AlbumEdit(),
    }

    curr_user = User.objects.get(pk=1)
    if request.method == "POST":
        if "song1_id" in request.POST:
            if FavoriteSong.objects.filter(pk=curr_user.pk):  # check if favorite song object exists for user
                song_instance = FavoriteSong.objects.get(pk=curr_user.pk)
                form = SongEdit(request.POST, request.FILES, instance=song_instance)
            else:
                form = SongEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

        elif "album1_id" in request.POST:
            if FavoriteAlbum.objects.filter(
                    pk=curr_user.pk
            ):  # check if favorite song object exists for user
                album_instance = FavoriteAlbum.objects.get(pk=curr_user.pk)
                form = AlbumEdit(request.POST, request.FILES, instance=album_instance)
            else:
                form = AlbumEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

        else:
            if FavoriteArtist.objects.filter(
                    pk=curr_user.pk
            ):  # check if favorite song object exists for user
                artist_instance = FavoriteArtist.objects.get(pk=curr_user.pk)
                form = ArtistEdit(request.POST, request.FILES, instance=artist_instance)
            else:
                form = ArtistEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

    return render(request, "application/profile_edit.html", context)


def profile(request):
    return render(request, "application/profile.html")
