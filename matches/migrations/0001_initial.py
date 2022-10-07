# Generated by Django 2.2.6 on 2019-10-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("home_team", models.CharField(max_length=200)),
                ("away_team", models.CharField(max_length=200)),
                ("score", models.CharField(max_length=10, null=True)),
                ("datetime", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
