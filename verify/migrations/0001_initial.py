# Generated by Django 2.1.1 on 2019-02-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signid', models.CharField(max_length=12, null=True, unique=True)),
            ],
        ),
    ]
