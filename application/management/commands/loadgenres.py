import csv
from django.core.management import BaseCommand
from application.models import GenreList


class Command(BaseCommand):
    help = (
        "Load a genres csv file into the database. use --path to specify the directory"
    )

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        with open(path, "rt") as f:
            reader = csv.reader(f, dialect="excel")
            for row in reader:
                GenreList.objects.create(genre_name=row[0])
