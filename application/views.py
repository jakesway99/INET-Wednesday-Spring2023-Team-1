from django.shortcuts import render, HttpResponse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def home(request):
    return HttpResponse("Hello, world. You're at the NYUBeatBuddies application!")


def profile_edit(request):
    client_credentials_manager = SpotifyClientCredentials()

    token_dict = client_credentials_manager.get_access_token()
    token = token_dict["access_token"]
    context = {"OAuth": token}
    return render(request, "application/profile_edit.html", context)


def profile(request):
    return render(request, "application/profile.html")
