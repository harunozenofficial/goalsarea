# Generated by Django 3.2.9 on 2021-11-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("matches", "0048_auto_20211107_1852"),
    ]

    operations = [
        migrations.AddField(
            model_name="videogoal",
            name="auto_moderator_comment_id",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
