# Generated by Django 2.0.1 on 2018-01-31 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_catalogueitem_catalogue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogue',
            old_name='year_of_publication_start',
            new_name='year_of_publication',
        ),
    ]
