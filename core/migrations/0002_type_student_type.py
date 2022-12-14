# Generated by Django 4.1.1 on 2022-11-19 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Type",
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
                ("title", models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name="student",
            name="type",
            field=models.ManyToManyField(blank=True, null=True, to="core.type"),
        ),
    ]
