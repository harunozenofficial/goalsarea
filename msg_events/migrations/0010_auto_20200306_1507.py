# Generated by Django 3.0.3 on 2020-03-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msg_events", "0009_auto_20200304_1745"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="author_filter",
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="webhook",
            name="author_filter",
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
