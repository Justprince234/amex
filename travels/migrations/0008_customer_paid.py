# Generated by Django 4.2.2 on 2023-07-21 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0007_flight_prices_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
