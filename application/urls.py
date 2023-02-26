from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    #path("", views.home, name="home"),
    path("", views.view_profile, name="view_profile"),
    path("profile/edit", views.profile_edit, name = "profile_edit")
=======
    path("", views.home, name="home"),
    path("profile/edit", views.profile_edit, name = "profile_edit"),
    path("profile", views.profile, name = "profile")
>>>>>>> 8af5a64e23770b92efe96ee1777537913f8f1db2
]
