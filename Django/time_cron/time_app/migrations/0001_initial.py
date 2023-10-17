# Generated by Django 4.2.4 on 2023-08-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PSTDateTime",
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
                ("datetime_field", models.DateTimeField()),
                ("tz", models.CharField(max_length=3)),
            ],
        ),
    ]