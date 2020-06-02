# Generated by Django 3.0.6 on 2020-05-14 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blogpost_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]