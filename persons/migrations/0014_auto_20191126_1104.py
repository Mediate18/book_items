# Generated by Django 2.0.13 on 2019-11-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0013_auto_20190912_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalperson',
            name='bibliography',
            field=models.TextField(blank=True, null=True, verbose_name='Bibiliography'),
        ),
        migrations.AddField(
            model_name='historicalperson',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='person',
            name='bibliography',
            field=models.TextField(blank=True, null=True, verbose_name='Bibiliography'),
        ),
        migrations.AddField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
    ]
