# Generated by Django 2.0 on 2018-12-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_auto_20181123_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_of_death',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Date of death'),
        ),
    ]
