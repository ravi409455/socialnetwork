# Generated by Django 5.0.6 on 2024-05-16 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="friendrequest",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2024, 5, 16, 15, 2, 21, 25830),
            ),
            preserve_default=False,
        ),
    ]