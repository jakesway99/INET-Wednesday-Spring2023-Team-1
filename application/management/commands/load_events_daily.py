from django.core.management import BaseCommand
from application.models import EventList
import os
import datetime
from .load_all_events import getTicketmaster


class Command(BaseCommand):
    help = "Load the T+31 day events from ticketmaster, deletes yesterday's events"

    def handle(self, *args, **kwargs):
        today = datetime.date.today()
        day = today + datetime.timedelta(days=31)
        tm_key = os.environ.get("TICKETMASTER_CLIENT_KEY1")
        event_list = getTicketmaster(day, day, tm_key)
        if not EventList.objects.filter(start_date=day):
            for event in event_list:
                event_inst = EventList(
                    event_name=event[0],
                    start_date=event[1],
                    start_time=event[2],
                    venue_name=event[3],
                    city=event[4],
                    img_url=event[5],
                )
                event_inst.save()

        yesterday = today - datetime.timedelta(days=1)
        EventList.objects.filter(start_date=yesterday).delete()
