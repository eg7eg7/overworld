# Generated by Django 2.2.1 on 2019-05-24 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_game_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='igdb',
            new_name='gb',
        ),
    ]
