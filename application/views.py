from django.shortcuts import render, HttpResponse
from spotipy.oauth2 import SpotifyClientCredentials
from .forms import SongEdit, ArtistEdit, AlbumEdit, GenreEdit
from .models import (
    User,
    FavoriteSong,
    FavoriteGenre,
    FavoriteAlbum,
    FavoriteArtist,
    GenreList,
)


def home(request):
    return HttpResponse("Hello, world. You're at the NYUBeatBuddies application!")


def profile_edit(request):
    client_credentials_manager = SpotifyClientCredentials()
    token_dict = client_credentials_manager.get_access_token()
    token = token_dict["access_token"]
    genres = GenreList.objects.all()

    curr_user = User.objects.get(pk=1)
    user_fav_songs = FavoriteSong.objects.get(user=curr_user)
    user_fav_artists = FavoriteArtist.objects.get(user=curr_user)
    user_fav_albums = FavoriteAlbum.objects.get(user=curr_user)
    user_fav_genres = FavoriteGenre.objects.get(user=curr_user)

    initial_songs = {
        "song1_name_artist": user_fav_songs.song1_name_artist,
        "song2_name_artist": user_fav_songs.song2_name_artist,
        "song3_name_artist": user_fav_songs.song3_name_artist,
        "song4_name_artist": user_fav_songs.song4_name_artist,
        "song5_name_artist": user_fav_songs.song5_name_artist,
        "song1_id": user_fav_songs.song1_id,
        "song2_id": user_fav_songs.song2_id,
        "song3_id": user_fav_songs.song3_id,
        "song4_id": user_fav_songs.song4_id,
        "song5_id": user_fav_songs.song5_id,
    }

    initial_artists = {
        "artist1_name": user_fav_artists.artist1_name,
        "artist2_name": user_fav_artists.artist2_name,
        "artist3_name": user_fav_artists.artist3_name,
        "artist4_name": user_fav_artists.artist4_name,
        "artist5_name": user_fav_artists.artist5_name,
        "artist1_id": user_fav_artists.artist1_id,
        "artist2_id": user_fav_artists.artist2_id,
        "artist3_id": user_fav_artists.artist3_id,
        "artist4_id": user_fav_artists.artist4_id,
        "artist5_id": user_fav_artists.artist5_id,
    }

    initial_albums = {
        "album1_name_artist": user_fav_albums.album1_name_artist,
        "album2_name_artist": user_fav_albums.album2_name_artist,
        "album3_name_artist": user_fav_albums.album3_name_artist,
        "album4_name_artist": user_fav_albums.album4_name_artist,
        "album5_name_artist": user_fav_albums.album5_name_artist,
        "album1_id": user_fav_albums.album1_id,
        "album2_id": user_fav_albums.album2_id,
        "album3_id": user_fav_albums.album3_id,
        "album4_id": user_fav_albums.album4_id,
        "album5_id": user_fav_albums.album5_id,
    }

    initial_genres = {
        "genre1": user_fav_genres.genre1,
        "genre2": user_fav_genres.genre2,
        "genre3": user_fav_genres.genre3,
        "genre4": user_fav_genres.genre4,
        "genre5": user_fav_genres.genre5,
    }
    if request.method == "GET":
        context = {
            "OAuth": token,
            "song_form": SongEdit(None, initial=initial_songs),
            "artist_form": ArtistEdit(None, initial=initial_artists),
            "album_form": AlbumEdit(None, initial=initial_albums),
            "genre_form": GenreEdit(None, initial=initial_genres),
            "genre_list": genres,
        }

    elif request.method == "POST":
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

            context = {  # set request.POST to whatever form is being posted
                "OAuth": token,
                "song_form": SongEdit(request.POST or None, initial=initial_songs),
                "artist_form": ArtistEdit(None, initial=initial_artists),
                "album_form": AlbumEdit(None, initial=initial_albums),
                "genre_form": GenreEdit(None, initial=initial_genres),
                "genre_list": genres,
            }

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

            context = {  # set request.POST to whatever form is being posted
                "OAuth": token,
                "song_form": SongEdit(None, initial=initial_songs),
                "artist_form": ArtistEdit(None, initial=initial_artists),
                "album_form": AlbumEdit(request.POST or None, initial=initial_albums),
                "genre_form": GenreEdit(None, initial=initial_genres),
                "genre_list": genres,
            }

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

            context = {  # set request.POST to whatever form is being posted
                "OAuth": token,
                "song_form": SongEdit(None, initial=initial_songs),
                "artist_form": ArtistEdit(None, initial=initial_artists),
                "album_form": AlbumEdit(None, initial=initial_albums),
                "genre_form": GenreEdit(request.POST or None, initial=initial_genres),
                "genre_list": genres,
            }

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

            context = {  # set request.POST to whatever form is being posted
                "OAuth": token,
                "song_form": SongEdit(None, initial=initial_songs),
                "artist_form": ArtistEdit(
                    request.POST or None, initial=initial_artists
                ),
                "album_form": AlbumEdit(None, initial=initial_albums),
                "genre_form": GenreEdit(None, initial=initial_genres),
                "genre_list": genres,
            }

    return render(request, "application/profile_edit.html", context)


def profile(request):
    return render(request, "application/profile.html")
