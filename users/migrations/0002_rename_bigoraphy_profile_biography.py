# Generated by Django 3.2.5 on 2021-07-21 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bigoraphy',
            new_name='biography',
        ),
    ]
