# Generated by Django 4.0.2 on 2022-02-21 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monitoring", "0007_performancemonitorevent"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="performancemonitorevent",
            options={"ordering": ("-timestamp",)},
        ),
        migrations.AlterField(
            model_name="performancemonitorevent",
            name="name",
            field=models.CharField(max_length=200),
        ),
    ]
