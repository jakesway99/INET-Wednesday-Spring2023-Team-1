import os

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from application.models import Account
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator

TEST_USER = os.environ["TEST_USER"]
TEST_USER_PASSWORD = os.environ["TEST_USER_PASSWORD"]


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username=TEST_USER, password=TEST_USER_PASSWORD
        )
        self.client = Client()
        self.account = Account.objects.create(
            user=self.user,
            first_name="testFirst",
            last_name="testLast",
            birth_year=1995,
        )

    def test_profile_edit_page(self):
        url_path = reverse("application:profile_edit")
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 302)
        self.client.login(username=TEST_USER, password=TEST_USER_PASSWORD)
        assert self.user.is_authenticated
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)

    def test_discover_people_page(self):
        url_path = reverse("application:discover")
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 302)
        self.client.login(username=TEST_USER, password=TEST_USER_PASSWORD)
        assert self.user.is_authenticated
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)

    # Julie tests (# maybe we already have this one?)
    # def test_user_logout(self):
    #     update_session(self.client, self.student.username, user_type=UserType.STUDENT)
    #     response = self.client.get(reverse("dashboard:logout"))
    #     self.assertRedirects(response, reverse("landingpage:index"))
    #     # test invalid access
    #     response = self.client.get(reverse("dashboard:dashboard"))
    #     self.assertRedirects(response, reverse("landingpage:index"))

    # want a return message saying invalid username or password and "return to Login"
    def test_invalid_login(self):
        url_path = reverse("application:discover")
        self.client.login(username=TEST_USER, password="dfgljk")
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 302)


class RegisterView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("account:register")

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_valid_login(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "@12345678",
            "password2": "@12345678",
        }
        response = self.client.post(self.url, data, follow=True)
        self.assertTemplateUsed(response, "registration/register.html")


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("account:login")
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass"
        )
        self.account = Account.objects.create(
            user=self.user,
            first_name="testFirst",
            last_name="testLast",
            birth_year=1995,
        )

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_valid_login(self):
        data = {"username": "testuser", "password": "testpass"}
        response = self.client.post(self.url, data, follow=True)
        self.assertRedirects(response, reverse("application:profile_edit"))

    def test_invalid_login(self):
        data = {"username": "testuser", "password": "wrongpass"}
        response = self.client.post(self.url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

        # self.assertContains(response, 'Please enter a correct username and password.')


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )
        self.client.force_login(self.user)

    def test_logout_view(self):
        response = self.client.get(reverse("account:logout"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")
        self.assertFalse("_auth_user_id" in self.client.session)


class ActivateAccountTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="testuser", email="testuser@example.com"
        )
        self.token = default_token_generator.make_token(self.user)

    def test_activation_success(self):
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = reverse(
            "account:activate",
            kwargs={
                "uidb64": uidb64,
                "token": self.token,
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.url, reverse("account:login"))
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_active)

    def test_activation_failure(self):
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = reverse(
            "account:activate",
            kwargs={
                "uidb64": uidb64,
                "token": self.token,
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.url, reverse("account:login"))
        self.user.refresh_from_db()