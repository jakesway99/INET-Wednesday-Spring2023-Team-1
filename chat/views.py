from django.shortcuts import render
from django.db.models import Q

from application.views import getMatchesData
from .models import Room, Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from application.models import Account


def getChatRoom(user1, user2):
    room = Room.objects.filter(
        (Q(started_by=user1) & Q(started_for=user2))
        | (Q(started_by=user2) & Q(started_for=user1))
    ).first()

    if room:
        return room

    room = Room.objects.create(started_by=user1, started_for=user2)
    room.save()
    return room


@login_required
def postMessage(request):
    print("\n\n\nGot a message\n\n\n")
    user = request.GET.get("user")
    user = User.objects.get(pk=user)
    room = request.GET.get("room")
    room = Room.objects.get(pk=room)
    content = request.GET.get("content")
    message = Message.objects.create(content=content, author=user, room=room)
    message.save()
    messages = room.messages.all()
    updated_messages = [
        {
            "id": message.pk,
            "content": message.content,
            "timestamp": message.timestamp,
            "author": message.author.pk,
            "room": message.room.pk,
            "is_read": message.is_read,
        }
        for message in messages
    ]
    return JsonResponse({"messages": updated_messages})


@login_required
def enterChat(request):
    friend_pk = request.GET.get("friend_pk")
    print("\n\n\nFRIEND_PK:", friend_pk, "\n\n\n")
    user = request.user
    account = Account.objects.get(user=user)
    matches_data = getMatchesData(user)
    friend = User.objects.get(pk=friend_pk)
    chat_room = getChatRoom(user, friend)
    user_data = Account.objects.get(user=user).__dict__
    user_data.pop("_state")
    context = {
        "messages": chat_room.messages.all(),
        "user": user_data,
        "room": chat_room,
    }
    context.update({"profile_picture": account.profile_picture})
    context.update({"matches_data": matches_data})
    return render(request, "chat/chatroom.html", context)
