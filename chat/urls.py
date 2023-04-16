from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("room", views.enterChat, name="room"),
    path("room/", views.enterChat, name="room"),
    path("postMessage/", views.postMessage, name="postMessage"),
    path("postMessage", views.postMessage, name="postMessage"),
]
