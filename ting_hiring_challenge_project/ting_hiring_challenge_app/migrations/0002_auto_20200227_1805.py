# Generated by Django 2.2.1 on 2020-02-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ting_hiring_challenge_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerregistration',
            name='player_mobile_no',
            field=models.CharField(blank='True', max_length=20),
        ),
        migrations.AlterField(
            model_name='playerregistration',
            name='player_name',
            field=models.CharField(blank='True', max_length=200),
        ),
    ]
