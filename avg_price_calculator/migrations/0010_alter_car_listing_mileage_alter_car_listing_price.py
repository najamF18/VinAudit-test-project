# Generated by Django 4.1.5 on 2023-01-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("avg_price_calculator", "0009_alter_car_dealer_vdp_last_seen_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="listing_mileage",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="listing_price",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
