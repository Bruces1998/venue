# Generated by Django 2.0.8 on 2019-03-20 15:53

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Halls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall_booking',
            name='requested_by',
        ),
        migrations.AddField(
            model_name='hall_booking',
            name='requested_by',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hall_booking',
            name='requested_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 20, 15, 53, 2, 687630, tzinfo=utc)),
        ),
    ]