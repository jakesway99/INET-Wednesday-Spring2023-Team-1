from django.urls import path
from . import views

urlpatterns = [
    path("room", views.enterChat, name="room"),
    path("room/", views.enterChat, name="room"),
    path("postMessage/", views.postMessage, name="postMessage"),
    path("postMessage", views.postMessage, name="postMessage"),
]
