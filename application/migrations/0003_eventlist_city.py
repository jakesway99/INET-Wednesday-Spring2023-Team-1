# Generated by Django 3.2.18 on 2023-04-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0002_eventlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventlist",
            name="city",
            field=models.CharField(default="new york", max_length=300),
            preserve_default=False,
        ),
    ]
