from django.shortcuts import render, HttpResponse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def home(request):
    return HttpResponse("Hello, world. You're at the NYUBeatBuddies application (on Julie's branch)")

def profile_edit(request):
    client_credentials_manager = SpotifyClientCredentials(client_id='17cb0114380b42dea06bdcc0c96ed786',
                                                          client_secret='6fcf10f9ddcd4c8f8ff20945c7eaaf01')

    tokenDict = client_credentials_manager.get_access_token()
    token = tokenDict['access_token']
    context = {'OAuth': token}
    return render(request, 'application/profile_edit.html',context)
