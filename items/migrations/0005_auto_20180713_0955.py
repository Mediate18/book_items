# Generated by Django 2.0 on 2018-07-13 09:55

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('persons', '0003_auto_20180703_0731'),
        ('items', '0004_auto_20180711_1505'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publication',
            new_name='Manifestation',
        ),
    ]
