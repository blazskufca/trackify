# Generated by Django 4.1.6 on 2023-02-05 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TrackedProducts",
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
                ("name", models.CharField(max_length=500, unique=True)),
                ("link", models.TextField(db_index=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=1000)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("modifiedDate", models.DateTimeField(auto_now=True)),
                ("priceHistory", models.JSONField()),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("items", models.ManyToManyField(to="tracker.trackedproducts")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
