# Generated by Django 4.2.3 on 2024-02-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("TourismApp", "0005_tour_start_city"),
    ]

    operations = [
        migrations.AddField(
            model_name="tour",
            name="price",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]