# Generated by Django 2.0 on 2018-02-15 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_auto_20180215_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookitem',
            old_name='catalogue_item',
            new_name='catalogue_entry',
        ),
    ]
