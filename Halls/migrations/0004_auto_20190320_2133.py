# Generated by Django 2.0.8 on 2019-03-20 16:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Halls', '0003_auto_20190320_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='booked_on',
        ),
        migrations.RemoveField(
            model_name='hall_booking',
            name='requested_by',
        ),
        migrations.AddField(
            model_name='hall_booking',
            name='requested_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hall_booking',
            name='requested_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 20, 16, 3, 36, 587515, tzinfo=utc)),
        ),
    ]
