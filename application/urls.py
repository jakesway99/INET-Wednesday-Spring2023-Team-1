from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/edit", views.profile_edit, name="profile_edit"),
    path("profile", views.profile, name="profile"),
    path("register", views.register_request, name="register"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    path("", include("django.contrib.auth.urls")),
]
