from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class FavoriteSong(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    song1_id = models.CharField(max_length=50)
    song1_name_artist = models.CharField(max_length=300)
    song2_id = models.CharField(max_length=50)
    song2_name_artist = models.CharField(max_length=300)
    song3_id = models.CharField(max_length=50)
    song3_name_artist = models.CharField(max_length=300)
    song4_id = models.CharField(max_length=50)
    song4_name_artist = models.CharField(max_length=300)
    song5_id = models.CharField(max_length=50)
    song5_name_artist = models.CharField(max_length=300)


class FavoriteArtist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    artist1_id = models.CharField(max_length=50)
    artist1_name = models.CharField(max_length=300)
    artist2_id = models.CharField(max_length=50)
    artist2_name = models.CharField(max_length=300)
    artist3_id = models.CharField(max_length=50)
    artist3_name = models.CharField(max_length=300)
    artist4_id = models.CharField(max_length=50)
    artist4_name = models.CharField(max_length=300)
    artist5_id = models.CharField(max_length=50)
    artist5_name = models.CharField(max_length=300)


class FavoriteAlbum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    album1_id = models.CharField(max_length=50)
    album1_name_artist = models.CharField(max_length=300)
    album2_id = models.CharField(max_length=50)
    album2_name_artist = models.CharField(max_length=300)
    album3_id = models.CharField(max_length=50)
    album3_name_artist = models.CharField(max_length=300)
    album4_id = models.CharField(max_length=50)
    album4_name_artist = models.CharField(max_length=300)
    album5_id = models.CharField(max_length=50)
    album5_name_artist = models.CharField(max_length=300)
