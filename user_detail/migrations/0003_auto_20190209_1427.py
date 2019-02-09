# Generated by Django 2.1.1 on 2019-02-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0002_auto_20190207_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='branch2',
            new_name='admission',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='email1',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='branch1',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='contact1',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='branch3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='leadername',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='participant2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='participant3',
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='signid',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
