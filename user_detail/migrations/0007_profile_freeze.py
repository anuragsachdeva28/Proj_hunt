# Generated by Django 2.1.1 on 2019-02-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0006_auto_20190212_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='freeze',
            field=models.BooleanField(default=False),
        ),
    ]