# Generated by Django 3.0.3 on 2020-03-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msg_events", "0006_auto_20200304_1530"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="destination",
            field=models.IntegerField(
                choices=[
                    (1, "Match"),
                    (2, "Video"),
                    (3, "Mirror"),
                    (4, "Video and Mirror"),
                ],
                default=1,
            ),
        ),
        migrations.AddField(
            model_name="tweet",
            name="link_regex",
            field=models.CharField(default=None, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name="webhook",
            name="link_regex",
            field=models.CharField(default=None, max_length=2000, null=True),
        ),
    ]
