# Generated by Django 2.0.8 on 2019-03-20 16:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Halls', '0005_auto_20190320_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall_booking',
            name='requested_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 20, 16, 17, 58, 460360, tzinfo=utc)),
        ),
    ]
