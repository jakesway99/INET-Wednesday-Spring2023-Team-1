from django import forms
from django.forms import ModelForm
from .models import *


class SongEdit(ModelForm):
    class Meta:
        model = FavoriteSong
        fields = ('song1_id', 'song2_id', 'song3_id', 'song4_id', 'song5_id', 'song1_name_artist', 'song2_name_artist',
                  'song3_name_artist', 'song4_name_artist', 'song5_name_artist')
        widgets = {'song1_id': forms.HiddenInput(), 'song2_id': forms.HiddenInput(),
                   'song3_id': forms.HiddenInput(), 'song4_id': forms.HiddenInput(),
                   'song5_id': forms.HiddenInput()}
        labels = {
            'song1_name_artist': "1", 'song2_name_artist': "2", 'song3_name_artist': "3", 'song4_name_artist': "4",
            'song5_name_artist': "5"
        }


class ArtistEdit(ModelForm):
    class Meta:
        model = FavoriteArtist
        fields = ('artist1_id', 'artist2_id', 'artist3_id', 'artist4_id', 'artist5_id', 'artist1_name', 'artist2_name',
                  'artist3_name', 'artist4_name', 'artist5_name')
        widgets = {'artist1_id': forms.HiddenInput(), 'artist2_id': forms.HiddenInput(),
                   'artist3_id': forms.HiddenInput(), 'artist4_id': forms.HiddenInput(),
                   'artist5_id': forms.HiddenInput()}
        labels = {
            'artist1_name': "1", 'artist2_name': "2", 'artist3_name': "3", 'artist4_name': "4",
            'artist5_name': "5"
        }


class AlbumEdit(ModelForm):
    class Meta:
        model = FavoriteAlbum
        fields = ('album1_id', 'album2_id', 'album3_id', 'album4_id', 'album5_id', 'album1_name_artist',
                  'album2_name_artist', 'album3_name_artist', 'album4_name_artist', 'album5_name_artist')
        widgets = {'album1_id': forms.HiddenInput(), 'album2_id': forms.HiddenInput(),
                   'album3_id': forms.HiddenInput(), 'album4_id': forms.HiddenInput(),
                   'album5_id': forms.HiddenInput()}
        labels = {
            'album1_name_artist': "1", 'album2_name_artist': "2", 'album3_name_artist': "3", 'album4_name_artist': "4",
            'album5_name_artist': "5"
        }
