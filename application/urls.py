from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("profile/edit", views.profile_edit, name="profile_edit"),
    path("profile", views.profile, name="profile"),
    path("discover", views.discover, name="discover"),
    path("next", views.getDiscoverProfile, name="next"),
    path("discover_events", views.discover_events, name="events"),
    path("profile/match/<int:match_pk>/", views.match_profile, name="match_profile"),
    path(
        "profile/match/remove/<int:match_pk>/", views.remove_match, name="remove_match"
    ),
]
