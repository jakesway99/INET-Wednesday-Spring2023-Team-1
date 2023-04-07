from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash

# import os
# from datetime import datetime
import calendar

# from django.contrib.auth.forms import PasswordChangeForm
import random
import datetime

# spotify api package
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .forms import (
    SongEdit,
    ArtistEdit,
    AlbumEdit,
    GenreEdit,
    PromptEdit,
    AccountSettingsForm,
    PasswordChangeForm,
)
from .models import (
    FavoriteSong,
    FavoriteGenre,
    FavoriteAlbum,
    FavoriteArtist,
    GenreList,
    UserPrompts,
    Account,
    Likes,
    EventList,
    SavedEvents,
)


def returnTime(time_string):
    if int(time_string[:2]) == 0:
        return_hr = str(12)
        am_pm = "AM"
    elif int(time_string[:2]) <= 11:
        return_hr = time_string[:2]
        am_pm = "AM"
    elif int(time_string[:2]) == 12:
        return_hr = time_string[:2]
        am_pm = "PM"
    else:
        return_hr = time_string[:2]
        am_pm = "PM"
    return return_hr + time_string[2:5] + am_pm


def get_pic(artist_id, spotify):
    artist = spotify.artist(artist_id)
    images = artist["images"]
    img_url = images[1]["url"]
    return img_url


def get_album_pic(album_id, spotify):
    album = spotify.album(album_id)
    images = album["images"]
    img_url = images[1]["url"]
    return img_url


def get_favorite_data(curr_user, spotify="", get_pics=False):
    if FavoriteSong.objects.filter(
        user=curr_user
    ):  # pre-populate edit form if data exists
        user_fav_songs = FavoriteSong.objects.get(user=curr_user)

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
    else:
        initial_songs = {}

    if FavoriteArtist.objects.filter(user=curr_user):
        user_fav_artists = FavoriteArtist.objects.get(user=curr_user)
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
    else:
        initial_artists = {}

    if FavoriteAlbum.objects.filter(user=curr_user):
        user_fav_albums = FavoriteAlbum.objects.get(user=curr_user)
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
    else:
        initial_albums = {}

    if FavoriteGenre.objects.filter(user=curr_user):
        user_fav_genres = FavoriteGenre.objects.get(user=curr_user)
        initial_genres = {
            "genre1": user_fav_genres.genre1,
            "genre2": user_fav_genres.genre2,
            "genre3": user_fav_genres.genre3,
            "genre4": user_fav_genres.genre4,
            "genre5": user_fav_genres.genre5,
        }
    else:
        initial_genres = {}

    if UserPrompts.objects.filter(user=curr_user):
        profile_prompts = UserPrompts.objects.get(user=curr_user)

        initial_prompts = {
            "prompt1": profile_prompts.prompt1,
            "prompt2": profile_prompts.prompt2,
            "prompt3": profile_prompts.prompt3,
            "prompt4": profile_prompts.prompt4,
            "prompt5": profile_prompts.prompt5,
            "response1": profile_prompts.response1,
            "response2": profile_prompts.response2,
            "response3": profile_prompts.response3,
            "response4": profile_prompts.response4,
            "response5": profile_prompts.response5,
        }
    else:
        initial_prompts = {}
    if get_pics:
        if initial_artists == {}:  # get artist artwork
            artist_imgs = {}
        else:
            artist_imgs = {
                # artist_images_list:
                "artist1_image_url": get_pic(initial_artists["artist1_id"], spotify),
                "artist2_image_url": get_pic(initial_artists["artist2_id"], spotify),
                "artist3_image_url": get_pic(initial_artists["artist3_id"], spotify),
                "artist4_image_url": get_pic(initial_artists["artist4_id"], spotify),
                "artist5_image_url": get_pic(initial_artists["artist5_id"], spotify),
            }
            # album_images_list:
        if initial_albums == {}:
            album_imgs = {}
        else:
            album_imgs = {
                "album1_image_url": get_album_pic(initial_albums["album1_id"], spotify),
                "album2_image_url": get_album_pic(initial_albums["album2_id"], spotify),
                "album3_image_url": get_album_pic(initial_albums["album3_id"], spotify),
                "album4_image_url": get_album_pic(initial_albums["album4_id"], spotify),
                "album5_image_url": get_album_pic(initial_albums["album5_id"], spotify),
            }
    else:
        artist_imgs = {}
        album_imgs = []

    return (
        initial_songs,
        initial_artists,
        initial_albums,
        initial_genres,
        initial_prompts,
        artist_imgs,
        album_imgs,
    )


def home(request):
    return HttpResponse("Hello, world. You're at the NYUBeatBuddies application!")


@login_required
def profile_edit(request):
    client_credentials_manager = SpotifyClientCredentials()
    token_dict = client_credentials_manager.get_access_token()
    token = token_dict["access_token"]
    in_password_change = False

    genres = GenreList.objects.all()

    curr_user = request.user
    (
        initial_songs,
        initial_artists,
        initial_albums,
        initial_genres,
        initial_prompts,
        _,
        _,
    ) = get_favorite_data(curr_user, False)

    initial_passw_info = {"old_password": curr_user.password}

    if Account.objects.filter(user=curr_user):
        account_inst = Account.objects.get(user=curr_user)
        initial_acct_info = {
            "first_name": account_inst.first_name,
            "last_name": account_inst.last_name,
            "birth_year": account_inst.birth_year,
            "location": account_inst.location,
            "profile_picture": account_inst.profile_picture,
        }
    else:
        initial_acct_info = {}

    if request.method == "GET":
        context = {
            "OAuth": token,
            "song_form": SongEdit(None, initial=initial_songs),
            "artist_form": ArtistEdit(None, initial=initial_artists),
            "album_form": AlbumEdit(None, initial=initial_albums),
            "genre_form": GenreEdit(None, initial=initial_genres),
            "prompt_form": PromptEdit(None, initial=initial_prompts),
            "account_edit": AccountSettingsForm(initial=initial_acct_info),
            "genre_list": genres,
            "passw_change": PasswordChangeForm(None, initial=initial_passw_info),
        }
        return render(request, "application/profile_edit.html", context)

    elif request.method == "POST":
        print("POST REQUEST: ", request.POST)
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

        if "album1_id" in request.POST:
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

        if "genre1" in request.POST:
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

        if "artist1_id" in request.POST:
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

        if "response1" in request.POST:
            if UserPrompts.objects.filter(
                user=curr_user
            ):  # check if favorite song object exists for user
                model_instance = UserPrompts.objects.get(user=curr_user)
                form = PromptEdit(request.POST, request.FILES, instance=model_instance)
            else:
                form = PromptEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

        if "first_name" in request.POST:
            if Account.objects.filter(
                user=curr_user
            ):  # check if favorite song object exists for user
                model_instance = Account.objects.get(user=curr_user)
                form = AccountSettingsForm(
                    request.POST, request.FILES, instance=model_instance
                )
            else:
                form = AccountSettingsForm(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

        if "old_password" in request.POST:
            in_password_change = True
            form2 = PasswordChangeForm(request.user, request.POST)
            form2.user = request.user
            context = {"form_passw": form2}

            if form2.is_valid():
                user = form2.save()
                update_session_auth_hash(request, user)  # so we dont logout the user
                messages.success(request, "Password changed successfully.")
            else:
                messages.error(
                    request,
                    "Password change unsuccessful. Please make sure you have entered"
                    " your old password"
                    " accurately and have followed the new password guidelines.",
                )
                # messages.error(request, form2.errors)

        if in_password_change is False:
            return redirect("application:profile")
        else:
            return redirect("application:profile_edit")


def getMatchesData(user):
    try:
        user_matches = list(Likes.objects.get(user=user).matches)
        if len(user_matches) == 0:
            raise Exception("No matches")
        matches_data = []
        for match in user_matches:
            matched_user = User.objects.get(pk=match)
            matched_user_account = Account.objects.get(user=matched_user)
            matches_data.append(
                {
                    "first_name": matched_user_account.first_name,
                    "last_name": matched_user_account.last_name,
                    "profile_picture": matched_user_account.profile_picture.url,
                    "pk": match,
                }
            )
    except Exception:
        matches_data = [
            {
                "first_name": "No Matches Yet",
                "last_name": "",
                "profile_picture": "https://nyu-beat-buddies-develop.s3.amazonaws.com/images/placeholder.png",
                "pk": user.pk,
            }
        ]
    return matches_data


@login_required
def profile(request):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    curr_user = request.user
    matches_data = getMatchesData(curr_user)

    interested_events, going_to_events = getSavedEvents(curr_user)

    user_data = Account.objects.get(user=curr_user).__dict__
    user_data.pop("_state")
    user_data["age"] = str(datetime.date.today().year - int(user_data["birth_year"]))
    (
        initial_songs,
        initial_artists,
        initial_albums,
        initial_genres,
        initial_prompts,
        artist_art,
        album_art,
    ) = get_favorite_data(curr_user, spotify, True)
    if (
        initial_artists == {}
        or initial_artists == {}
        or initial_albums == {}
        or initial_genres == {}
        or initial_prompts == {}
    ):
        return redirect("application:profile_edit")
    account = Account.objects.get(user=curr_user)
    context = {}
    context.update(initial_songs)
    context.update(initial_artists)
    context.update(initial_albums)
    context.update(initial_genres)
    context.update(initial_prompts)
    context.update(artist_art)
    context.update(album_art)
    context.update({"user": user_data})
    context.update({"matches_data": matches_data})
    context.update({"profile_picture": account.profile_picture})
    context.update({"interested_events": interested_events})
    context.update({"going_to_events": going_to_events})
    return render(request, "application/profile.html", context)


@login_required
def discover(request):
    global CURRENT_DISCOVER
    CURRENT_DISCOVER = getNextUserPk(request)
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    curr_user = request.user
    matches_data = getMatchesData(curr_user)
    user_data = Account.objects.get(user=curr_user).__dict__
    user_data.pop("_state")
    user_data["age"] = str(datetime.date.today().year - int(user_data["birth_year"]))
    discover_user = User.objects.get(pk=CURRENT_DISCOVER)
    discover_user_data = Account.objects.get(user=discover_user).__dict__
    discover_user_data.pop("_state")
    discover_user_data["age"] = str(
        datetime.date.today().year - int(discover_user_data["birth_year"])
    )

    (
        initial_songs,
        initial_artists,
        initial_albums,
        initial_genres,
        initial_prompts,
        artist_art,
        album_art,
    ) = get_favorite_data(discover_user, spotify, True)
    interested_events, going_to_events = getSavedEvents(discover_user)

    account = Account.objects.get(user=curr_user)
    discover_account = Account.objects.get(user=discover_user)
    context = {}
    context.update(initial_songs)
    context.update(initial_artists)
    context.update(initial_albums)
    context.update(initial_genres)
    context.update(initial_prompts)
    context.update(artist_art)
    context.update(album_art)
    context.update({"user": user_data})
    context.update({"discover_user": discover_user_data})
    context.update({"matches_data": matches_data})
    context.update({"profile_picture": account.profile_picture})
    context.update({"discover_profile_picture": discover_account.profile_picture})
    context.update({"interested_events": interested_events})
    context.update({"going_to_events": going_to_events})
    return render(request, "application/discover.html", context)


@login_required
def getNextUserPk(request):
    curr_user = request.user
    try:
        likes = Likes.objects.get(user=curr_user)
    except Exception:
        likes = Likes.objects.create(user=curr_user)
    if likes.likes is not None or likes.dislikes is not None:
        if likes.likes is not None and likes.dislikes is not None:
            previous_likes_and_dislikes = likes.likes + likes.dislikes
        else:
            previous_likes_and_dislikes = (
                likes.likes if likes.likes is not None else likes.dislikes
            )
    else:
        previous_likes_and_dislikes = []
    previous_likes_and_dislikes.append(curr_user.pk)
    all_users_pks = list(
        User.objects.filter(is_superuser=False).values_list("pk", flat=True)
    )
    if len(all_users_pks) - len(previous_likes_and_dislikes) < 1:
        return curr_user.pk
    for pk in previous_likes_and_dislikes:
        if pk in all_users_pks:
            all_users_pks.remove(pk)
    random_user_pk = random.choice(all_users_pks)
    return random_user_pk


@login_required
def getDiscoverProfile(request):
    is_match = False
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    curr_user = request.user

    # Save current decision
    global CURRENT_DISCOVER
    discover_user = User.objects.get(pk=CURRENT_DISCOVER)
    try:
        discover_user_likes = Likes.objects.get(user=discover_user)
    except Exception:
        discover_user_likes = Likes.objects.create(user=discover_user)
    try:
        likes = Likes.objects.get(user=curr_user)
    except Exception:
        likes = Likes.objects.create(user=curr_user)
    likes.likes = [] if likes.likes is None else likes.likes
    likes.dislikes = [] if likes.dislikes is None else likes.dislikes
    likes.matches = [] if likes.matches is None else likes.matches
    discover_user_likes.likes = (
        [] if discover_user_likes.likes is None else discover_user_likes.likes
    )
    discover_user_likes.dislikes = (
        [] if discover_user_likes.dislikes is None else discover_user_likes.dislikes
    )
    discover_user_likes.matches = (
        [] if discover_user_likes.matches is None else discover_user_likes.matches
    )
    if (
        request.GET.get("action") == "like"
        and CURRENT_DISCOVER not in likes.likes
        and CURRENT_DISCOVER != curr_user.pk
        and not curr_user.is_superuser
    ):
        likes.likes.append(int(CURRENT_DISCOVER))
        if curr_user.pk in discover_user_likes.likes:
            discover_user_likes.matches.append(curr_user.pk)
            discover_user_likes.save()
            likes.matches.append(int(CURRENT_DISCOVER))
            likes.save()
            is_match = True

    elif (
        request.GET.get("action") == "dislike"
        and CURRENT_DISCOVER not in likes.dislikes
        and CURRENT_DISCOVER != curr_user.pk
        and not curr_user.is_superuser
    ):
        likes.dislikes.append(int(CURRENT_DISCOVER))
    likes.save()

    # Get a random user not seen before
    next_user_pk = getNextUserPk(request)
    next_user = User.objects.get(pk=next_user_pk)
    interested_events, going_to_events = getSavedEvents(next_user)

    # Pass next user to front end
    CURRENT_DISCOVER = next_user.pk
    (
        next_favorite_songs,
        next_favorite_artists,
        next_favorite_albums,
        next_favorite_genres,
        next_next_prompts,
        next_next_artist_imgs,
        next_album_imgs,
    ) = get_favorite_data(next_user, spotify, True)
    updated_matches = getMatchesData(curr_user)
    next_user_data = Account.objects.get(user=next_user)
    previous_user_data = Account.objects.get(user=discover_user)
    image_url = next_user_data.profile_picture.url
    next_user_data = next_user_data.__dict__
    next_user_data.pop("_state")
    next_user_data["profile_picture"] = image_url
    context = {
        "discover_user": next_user_data,
        "discover_favorite_songs": next_favorite_songs,
        "discover_favorite_artists": next_favorite_artists,
        "discover_favorite_albums": next_favorite_albums,
        "discover_favorite_genres": next_favorite_genres,
        "discover_prompts": next_next_prompts,
        "discover_artist_imgs": next_next_artist_imgs,
        "discover_albums_imgs": next_album_imgs,
        "updated_matches": updated_matches,
        "is_match": is_match,
        "previous_user": {
            "first_name": previous_user_data.first_name,
            "last_name": previous_user_data.last_name,
            "profile_picture": previous_user_data.profile_picture.url,
            "pk": discover_user.pk,
        },
    }
    context.update({"interested_events": interested_events})
    context.update({"going_to_events": going_to_events})
    return JsonResponse(context)


@login_required
def discover_events(request):
    event_list = []
    all_events = EventList.objects.all()
    for event in all_events:
        time_string = event.start_time
        if time_string == "TBA":
            event_time_final = "TBA"
        else:
            # getting stripped standard time from datetime obj
            time_object = datetime.datetime.strptime(event.start_time, "%H:%M:%S")
            mil_time = time_object.time()
            std_time = mil_time.strftime("%-I:%M" "%p").lower()
            event_time_final = std_time

        # getting month name and day number from datetime obj
        month_num = event.start_date.month
        month_name = calendar.month_abbr[month_num]
        day_num = event.start_date.day

        # getting day of the week based on datetime obj
        dow_num = event.start_date.weekday()
        day_name = calendar.day_abbr[dow_num]

        event_list.append(
            (
                event.event_name,
                month_name,
                day_num,
                day_name,
                event_time_final,
                event.venue_name,
                event.city,
                event.img_url,
                event.pk,
            )
        )
    curr_user = request.user
    account = Account.objects.get(user=curr_user)
    interested_events, going_to_events = getSavedEvents(curr_user)

    context = {}
    context.update({"profile_picture": account.profile_picture})
    context.update({"first_name": account.first_name})
    context.update({"event_list": event_list})
    context.update({"interested_events": interested_events})
    context.update({"going_to_events": going_to_events})

    return render(request, "application/discover_events.html", context)


@login_required
def match_profile(request, match_pk):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    curr_user = request.user
    curr_user_matches = Likes.objects.get(user=curr_user).matches
    if match_pk not in curr_user_matches:
        return redirect("application:discover")
    matches_data = getMatchesData(curr_user)
    user_data = Account.objects.get(user=curr_user).__dict__
    user_data.pop("_state")
    user_data["age"] = str(datetime.date.today().year - int(user_data["birth_year"]))
    matched_user = User.objects.get(pk=match_pk)
    matched_user_data = Account.objects.get(user=matched_user).__dict__
    matched_user_data.pop("_state")
    matched_user_data["age"] = str(
        datetime.date.today().year - int(matched_user_data["birth_year"])
    )

    (
        initial_songs,
        initial_artists,
        initial_albums,
        initial_genres,
        initial_prompts,
        artist_art,
        album_art,
    ) = get_favorite_data(matched_user, spotify, True)

    account = Account.objects.get(user=curr_user)
    matched_account = Account.objects.get(user=matched_user)
    interested_events, going_to_events = getSavedEvents(matched_user)

    context = {}
    context.update(initial_songs)
    context.update(initial_artists)
    context.update(initial_albums)
    context.update(initial_genres)
    context.update(initial_prompts)
    context.update(artist_art)
    context.update(album_art)
    context.update({"user": user_data})
    context.update({"matched_user": matched_user_data})
    context.update({"matches_data": matches_data})
    context.update({"profile_picture": account.profile_picture})
    context.update({"matched_profile_picture": matched_account.profile_picture})
    context.update({"interested_events": interested_events})
    context.update({"going_to_events": going_to_events})
    return render(request, "application/match_profile.html", context)


@login_required
def remove_match(request, match_pk):
    user_likes = Likes.objects.get(user=request.user)
    user_likes.likes.remove(int(match_pk))
    user_likes.matches.remove(int(match_pk))
    user_likes.save()
    return redirect("application:discover")


def getSavedEvents(user):
    try:
        saved_events = SavedEvents.objects.get(user=user)
    except Exception:
        saved_events = SavedEvents.objects.create(user=user)

    interestedEvents = (
        [] if saved_events.interestedEvents is None else saved_events.interestedEvents
    )
    goingToEvents = (
        [] if saved_events.goingToEvents is None else saved_events.goingToEvents
    )
    interested_events = getEventList(interestedEvents)
    going_to_events = getEventList(goingToEvents)

    return interested_events, going_to_events


def getEventList(user_events):
    saved_events = []
    for event_id in user_events:
        event = EventList.objects.get(pk=event_id)
        time_string = event.start_time
        if time_string == "TBA":
            event_time_final = "TBA"
        else:
            # getting stripped standard time from datetime obj
            time_object = datetime.datetime.strptime(event.start_time, "%H:%M:%S")
            mil_time = time_object.time()
            std_time = mil_time.strftime("%-I:%M" "%p").lower()
            event_time_final = std_time
        saved_events.append(
            (
                event.event_name,
                calendar.month_abbr[event.start_date.month],
                event.start_date.day,
                calendar.day_abbr[event.start_date.weekday()],
                event_time_final,
                event.venue_name,
                event.city,
                event.img_url,
                event.pk,
            )
        )
    return saved_events

    @login_required
    def save_event(request, event_id):
        saved_events = SavedEvents.objects.get(user=request.user).interestedEvents
        saved_events.interestedEvents.add(event_id)
        saved_events.save()
        return redirect("application:discover_events")
