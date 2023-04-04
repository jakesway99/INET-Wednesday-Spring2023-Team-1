from django.core.management import BaseCommand
from application.models import EventList
import os
import datetime
import time
import requests


def getTicketmaster(start_date, end_date, tm_key):
    event_list = []
    search_string = (
        f"https://app.ticketmaster.com/discovery/v2/events.json?startDateTime={start_date}"
        f"T00%3A00%3A00Z&endDateTime={end_date}T23%3A59%3A59Z&classification"
        f"Name=music&city=New+York&sort=date%2Casc&apikey={tm_key}"
    )
    response = requests.get(search_string)
    result = response.json()
    total_pages = result["page"]["totalPages"]
    for page in range(total_pages):
        for event in result["_embedded"]["events"]:
            img_url = ""
            for img in event["images"]:
                if (
                        "RETINA_PORTRAIT" in img["url"]
                        and img["width"] == 640
                        and img["height"] == 360
                ):
                    img_url = img["url"]
                    break

            event_dates = event["dates"]["start"]
            if event_dates.get("localTime") is None:
                start_time = 'TBA'
            else:
                start_time = event["dates"]["start"]["localTime"]

            event_info = (
                event["name"],
                datetime.datetime.strptime(
                    event["dates"]["start"]["localDate"], "%Y-%m-%d"
                ).date(),
                start_time,
                event["_embedded"]["venues"][0]["name"],
                event["_embedded"]["venues"][0]["city"]["name"],
                img_url,
            )
            event_list.append(event_info)

        if page != total_pages - 1:
            next_link = result["_links"]["next"]["href"]
            next_string = f"https://app.ticketmaster.com{next_link}&apikey={tm_key}"
            result = requests.get(next_string).json()
        time.sleep(0.2)
    return event_list


class Command(BaseCommand):
    help = "Load events for t+30 days from ticketmaster api into database"

    def handle(self, *args, **kwargs):
        today = datetime.date.today()
        tm_key = os.environ.get("TICKETMASTER_CLIENT_KEY1")
        event_list = getTicketmaster(today, today + datetime.timedelta(days=30), tm_key)
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

