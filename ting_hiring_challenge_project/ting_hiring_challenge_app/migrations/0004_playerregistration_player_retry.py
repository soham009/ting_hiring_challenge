# Generated by Django 2.2 on 2020-02-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ting_hiring_challenge_app', '0003_playerregistration_player_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerregistration',
            name='player_retry',
            field=models.BooleanField(default=True),
        ),
    ]
