# Generated by Django 2.1.1 on 2019-02-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0013_auto_20190215_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lastsub',
            field=models.DateTimeField(auto_now=True),
        ),
    ]