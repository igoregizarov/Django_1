# Generated by Django 3.1.4 on 2021-01-04 16:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20201220_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activations_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 16, 51, 43, 136052, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveSmallIntegerField(default=18, verbose_name='возраст'),
        ),
    ]
