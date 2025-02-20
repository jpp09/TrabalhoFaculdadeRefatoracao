# Generated by Django 5.1.6 on 2025-02-19 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="comentarios",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cometario", models.CharField(max_length=250)),
                (
                    "data_publicacao",
                    models.DateField(
                        default=datetime.datetime(2025, 2, 19, 22, 35, 42, 467959)
                    ),
                ),
            ],
        ),
    ]
