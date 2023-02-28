# Generated by Django 4.1.7 on 2023-02-28 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0008_alter_favoritesong_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favoritealbum",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="application.user"
            ),
        ),
        migrations.AlterField(
            model_name="favoriteartist",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="application.user"
            ),
        ),
    ]
