# Generated by Django 3.0.3 on 2020-03-04 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("matches", "0024_auto_20200303_1227"),
    ]

    operations = [
        migrations.DeleteModel(
            name="WebhookUrl",
        ),
    ]
