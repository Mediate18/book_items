# Generated by Django 2.0 on 2018-02-15 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_auto_20180215_0907'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CatalogueItem',
            new_name='CatalogueEntry',
        ),
    ]
