# Generated by Django 3.0.6 on 2020-05-21 10:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200521_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 10, 32, 0, 758483, tzinfo=utc)),
        ),
    ]
