from django.urls import path, include
from . import views

urlpatterns = [
    path("login/register", views.register_request, name="register"),
    path("login", views.login_view, name="login"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    path("", include("django.contrib.auth.urls")),
]
