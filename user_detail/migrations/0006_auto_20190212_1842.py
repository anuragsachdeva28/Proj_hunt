# Generated by Django 2.1.1 on 2019-02-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0005_auto_20190212_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='attempts',
            field=models.IntegerField(default=0),
        ),
    ]