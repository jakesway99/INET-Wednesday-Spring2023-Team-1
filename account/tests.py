import os

from django.test import TestCase, Client
from django.urls import reverse

TEST_USER = os.environ["TEST_USER"]
TEST_USER_PASSWORD = os.environ["TEST_USER_PASSWORD"]


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_valid_login_student(self):
        data = {"username": TEST_USER, "password": TEST_USER_PASSWORD}
        url = reverse("account:login")
        response = self.client.get(url)
        self.assertTrue(response, 200)
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
