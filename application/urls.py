from django.urls import path
from . import views

urlpatterns = [
    #path("", views.home, name="home"),
    path("", views.view_profile, name="view_profile"),
    path("profile/edit", views.profile_edit, name = "profile_edit")
]
