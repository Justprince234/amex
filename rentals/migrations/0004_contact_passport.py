# Generated by Django 4.2.2 on 2023-07-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='passport',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
