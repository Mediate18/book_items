# Generated by Django 2.0 on 2018-02-19 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_auto_20180215_0944'),
    ]

    operations = [
        migrations.RenameModel('BookItem', 'Item'),
    ]
