# Generated by Django 2.1.1 on 2019-02-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0017_profile_rules'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='q1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='q2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='q3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='q4',
            field=models.BooleanField(default=False),
        ),
    ]
