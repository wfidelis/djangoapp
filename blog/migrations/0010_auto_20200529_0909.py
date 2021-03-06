# Generated by Django 3.0.6 on 2020-05-29 09:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20200521_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 29, 9, 9, 16, 999267, tzinfo=utc)),
        ),
    ]
