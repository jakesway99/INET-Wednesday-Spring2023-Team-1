from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(FavoriteSong)
admin.site.register(FavoriteAlbum)
admin.site.register(FavoriteArtist)
# Register your models here.
