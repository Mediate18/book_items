# Generated by Django 2.0 on 2018-05-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='viaf_id',
            field=models.CharField(blank=True, max_length=32, verbose_name='VIAF ID of a work'),
        ),
    ]
