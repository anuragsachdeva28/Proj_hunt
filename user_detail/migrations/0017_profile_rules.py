# Generated by Django 2.1.1 on 2019-02-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0016_auto_20190215_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rules',
            field=models.BooleanField(default=False),
        ),
    ]
