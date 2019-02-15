# Generated by Django 2.1.1 on 2019-02-15 14:40

import Questions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0003_auto_20190212_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_model',
            name='image',
        ),
        migrations.AddField(
            model_name='question_model',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=Questions.models.upload_image_path),
        ),
    ]