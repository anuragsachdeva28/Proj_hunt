# Generated by Django 2.1.1 on 2019-02-15 12:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0011_auto_20190215_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lastsub',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 12, 23, 35, 238265, tzinfo=utc)),
        ),
    ]
