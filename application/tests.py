from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import FavoriteGenre, FavoriteArtist, FavoriteSong, FavoriteAlbum, Account
import os

# from bs4 import BeautifulSoup

TEST_USER = os.environ["TEST_USER"]
TEST_USER_PASSWORD = os.environ["TEST_USER_PASSWORD"]


class HomeTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username=TEST_USER, password=TEST_USER_PASSWORD
        )
        self.url = "/"

    def test_profile_response_not_logged_in(self):
        response = self.client.get("/application/profile")
        self.assertEqual(response.status_code, 302)

    def test_profile_response(self):
        response = self.client.get(self.url)
        # Test if the response status code is 301 - redirect to login
        self.assertEqual(response.status_code, 301)

    def test_account_register_page_exists(self):
        response = self.client.get("/account/register")
        self.assertEqual(response.status_code, 200)

    def test_account_login_page_exists(self):
        response = self.client.get("/account/login")
        self.assertEqual(response.status_code, 200)

    # def test_account_login_page_exists(self):
    #     self.client.login(username=TEST_USER, password=TEST_USER_PASSWORD)
    #     response = self.client.get("/application/profile")
    #     self.assertEqual(response.status_code, 302)

    def test_matches_section_exists(self):
        # response = self.client.get(self.url)
        # soup = BeautifulSoup(response.content, "html.parser")
        # heading = soup.select_one("h2")
        # self.assertIsNotNone(heading)
        # self.assertEqual(heading.text, "Matches")
        return

    def test_meaningful_song_exists(self):
        # response = self.client.get(self.url)
        # Test if the response status code is 200
        # self.assertEqual(response.status_code, 200)
        # Test if the response contains the expected heading and paragraph
        # soup = BeautifulSoup(response.content, "html.parser")
        # heading = soup.select_one("h4")
        # self.assertIsNotNone(heading)
        # self.assertEqual(heading.text, "A song that has meaning to you")
        return

    # def test_discover_people_exists(self):
    #     response = self.client.get('/application/profile')
    #     self.assertEqual(response.status_code, 200)
    #     soup = BeautifulSoup(response.content, "html.parser")
    #     button = soup.select_one('button')
    #     self.assertIsNotNone(button)
    #     # self.assertEqual(button.text, "Discover People")


class Profile(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("application:profile_edit")
        self.user = User.objects.create_user(
            username="testuser", password="@12345678", email="testing123@example.com"
        )
        self.account = Account.objects.create(
            user=self.user,
            first_name="testFirst",
            last_name="testLast",
            birth_year=1995,
        )

    def test_add_profile_edit(self):
        data = {"username": "testuser", "password": "@12345678"}
        response = self.client.post(reverse("account:login"), data, follow=True)

        data = {
            "song1_name_artist": "Kill Bill - SZA",
            "song2_name_artist": "Sure Thing - Miguel",
            "song3_name_artist": "Whenever, Wherever - Shakira",
            "song4_name_artist": "Wasted On You - Morgan Wallen",
            "song5_name_artist": "And We Knew It Was Our Time - Lane 8, Massane",
            "song1_id": "3OHfY25tqY28d16oZczHc8",
            "song2_id": "0JXXNGljqupsJaZsgSbMZV",
            "song3_id": "2lnzGkdtDj5mtlcOW2yRtG",
            "song4_id": "3cBsEDNhFI9E82vPj3kvi3",
            "song5_id": "2tIv3DITNBTTayAM6Rewqi",
            "album1_name_artist": "Endless Summer Vacation - Miley Cyrus",
            "album2_name_artist": "evermore - Taylor Swift",
            "album3_name_artist": "Purple (Rainbow Friends) - Rockit Music",
            "album4_name_artist": "RENAISSANCE - Beyoncé",
            "album5_name_artist": "Bluey the Album - Bluey",
            "album1_id": "0HiZ8fNXwJOQcrf5iflrdz",
            "album2_id": "5jmVg7rwRcgd6ARPAeYNSm",
            "album3_id": "0uw5PIXZiA3Kp8B6qBqPIo",
            "album4_id": "6FJxoadUE4JNVwWHghBwnb",
            "album5_id": "4ke6cauk7sHuydZCrkgD7s",
            "artist1_name": "Harry Styles",
            "artist2_name": "Taylor Swift",
            "artist3_name": "The 1975",
            "artist4_name": "The Weeknd",
            "artist5_name": "BTS",
            "artist1_id": "6KImCVD70vtIoJWnq6nGn3",
            "artist2_id": "6KImCVD70vtIoJWnq6nGn3",
            "artist3_id": "3mIj9lX2MWuHmhNCA7LSCW",
            "artist4_id": "1Xyo4u8uXC1ZmMpatF05PJ",
            "artist5_id": "3Nrfpe0tUJi4K4DXYWgMUX",
            "genre1": "pop",
            "genre2": "vaporwave",
            "genre3": "melodic dubstep",
            "genre4": "pop rock",
            "genre5": "kpop",
            "response5": "Nothing Else Matters (Remastered) - Metallica",
            "first_name": "John",
            "last_name": "Doe",
            "birth_year": "1990",
            "location": "Bushwick",
        }
        response = self.client.post(self.url, data, follows=True)
        self.assertEqual(response.status_code, 302)

        fav_song = FavoriteSong.objects.get(user=self.user)
        self.assertEqual(fav_song.song1_name_artist, "Kill Bill - SZA")
        self.assertEqual(fav_song.song3_name_artist, "Whenever, Wherever - Shakira")
        self.assertEqual(
            fav_song.song5_name_artist, "And We Knew It Was Our Time - Lane 8, Massane"
        )
        self.assertEqual(fav_song.song1_id, "3OHfY25tqY28d16oZczHc8")
        self.assertEqual(fav_song.song3_id, "2lnzGkdtDj5mtlcOW2yRtG")
        self.assertEqual(fav_song.song5_id, "2tIv3DITNBTTayAM6Rewqi")

        fav_album = FavoriteAlbum.objects.get(user=self.user)
        self.assertEqual(
            fav_album.album1_name_artist, "Endless Summer Vacation - Miley Cyrus"
        )
        self.assertEqual(
            fav_album.album3_name_artist, "Purple (Rainbow Friends) - Rockit Music"
        )
        self.assertEqual(fav_album.album5_name_artist, "Bluey the Album - Bluey")
        self.assertEqual(fav_album.album1_id, "0HiZ8fNXwJOQcrf5iflrdz")
        self.assertEqual(fav_album.album5_id, "4ke6cauk7sHuydZCrkgD7s")

        fav_artist = FavoriteArtist.objects.get(user=self.user)
        self.assertEqual(fav_artist.artist1_name, "Harry Styles")
        self.assertEqual(fav_artist.artist5_name, "BTS")
        self.assertEqual(fav_artist.artist1_id, "6KImCVD70vtIoJWnq6nGn3")
        self.assertEqual(fav_artist.artist5_id, "3Nrfpe0tUJi4K4DXYWgMUX")

        fav_genre = FavoriteGenre.objects.get(user=self.user)
        self.assertEqual(fav_genre.genre1, "pop")
        self.assertEqual(fav_genre.genre2, "vaporwave")
        self.assertEqual(fav_genre.genre5, "kpop")


class DiscoverEvents(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="TEST_USER", password="@1234567")

    def test_discover_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("application:events"))
        self.assertEqual(response.status_code, 200)
