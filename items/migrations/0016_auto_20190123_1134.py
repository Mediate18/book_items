# Generated by Django 2.0 on 2019-01-23 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_auto_20181219_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogues.Collection'),
        ),
    ]
