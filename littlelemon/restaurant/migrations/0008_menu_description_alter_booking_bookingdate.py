# Generated by Django 4.2.1 on 2023-07-11 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_booking_bookingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(default='Deliciousness passed down to us from our great forefathers from Modenna,Italy', max_length=500),
        ),
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 11, 14, 52, 50, 765589)),
        ),
    ]
