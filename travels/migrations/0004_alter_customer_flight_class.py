# Generated by Django 4.2.2 on 2023-07-21 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0003_customer_flight_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='flight_class',
            field=models.CharField(max_length=100),
        ),
    ]
