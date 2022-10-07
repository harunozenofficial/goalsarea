# Generated by Django 3.0.3 on 2020-03-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monitoring", "0002_remove_matchnotfound_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="MonitoringAccount",
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
                ("title", models.CharField(max_length=200, unique=True)),
                ("telegram_bot_key", models.CharField(max_length=1024, unique=True)),
                ("telegram_user_ud", models.IntegerField(null=True)),
            ],
        ),
    ]
