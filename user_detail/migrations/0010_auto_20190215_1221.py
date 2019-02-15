# Generated by Django 2.1.1 on 2019-02-15 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0009_profile_freeze'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-points', '-lastsub']},
        ),
        migrations.AddField(
            model_name='profile',
            name='lastsub',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 12, 21, 55, 211388)),
        ),
    ]
