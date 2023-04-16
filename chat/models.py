from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    started_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rooms_started_by"
    )
    started_for = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rooms_started_for"
    )


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["timestamp"]
