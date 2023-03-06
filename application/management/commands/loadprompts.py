import csv
from django.core.management import BaseCommand
from application.models import PromptList


class Command(BaseCommand):
    help = (
        "Load a music prompts csv file into the database. "
        "use --path to specify the directory"
    )

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        with open(path, "rt") as f:
            reader = csv.reader(f, dialect="excel")
            for row in reader:
                PromptList.objects.create(prompt=row[0])
