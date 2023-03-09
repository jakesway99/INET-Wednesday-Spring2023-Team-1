from django.test import TestCase, Client
from bs4 import BeautifulSoup


class HomeTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/application/profile"

    def test_profile_response(self):
        response = self.client.get(self.url)

        # Test if the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_matches_section_exists(self):
        response = self.client.get(self.url)
        #soup = BeautifulSoup(response.content, "html.parser")
        #heading = soup.select_one("h2")
        #self.assertIsNotNone(heading)
        #self.assertEqual(heading.text, "Matches")

    def test_meaningful_song_exists(self):
        response = self.client.get(self.url)
        # Test if the response status code is 200
        self.assertEqual(response.status_code, 200)
        # Test if the response contains the expected heading and paragraph
        #soup = BeautifulSoup(response.content, "html.parser")
        #heading = soup.select_one("h4")
        #self.assertIsNotNone(heading)
        #self.assertEqual(heading.text, "A song that has meaning to you")
