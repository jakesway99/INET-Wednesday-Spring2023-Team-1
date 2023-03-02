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
    genres = GenreList.objects.all()
    context = {
        "OAuth": token,
        "song_form": SongEdit(),
        "artist_form": ArtistEdit(),
        "album_form": AlbumEdit(),
        "genre_form": GenreEdit(),
        "genre_list": genres,
    }

    curr_user = User.objects.get(pk=1)
    if request.method == "POST":
        if "song1_id" in request.POST:  # check which submit button was pressed on page
            if FavoriteSong.objects.filter(  # check if favorite song object exists for user
                user=curr_user
            ):
                model_instance = FavoriteSong.objects.get(user=curr_user)
                form = SongEdit(request.POST, request.FILES, instance=model_instance)
            else:
                form = SongEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(
                    commit=False
                )  # don't form yet, add user first
                profile_update.user = curr_user
                profile_update.save()

        elif "album1_id" in request.POST:
            if FavoriteAlbum.objects.filter(
                user=curr_user
            ):  # check if favorite song object exists for user
                model_instance = FavoriteAlbum.objects.get(user=curr_user)
                form = AlbumEdit(request.POST, request.FILES, instance=model_instance)
            else:
                form = AlbumEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

        elif "genre1" in request.POST:
            if FavoriteGenre.objects.filter(
                user=curr_user
            ):  # check if favorite song object exists for user
                model_instance = FavoriteGenre.objects.get(user=curr_user)
                form = GenreEdit(request.POST, request.FILES, instance=model_instance)
            else:
                form = GenreEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

        else:
            if FavoriteArtist.objects.filter(
                user=curr_user
            ):  # check if favorite song object exists for user
                model_instance = FavoriteArtist.objects.get(user=curr_user)
                form = ArtistEdit(request.POST, request.FILES, instance=model_instance)
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
