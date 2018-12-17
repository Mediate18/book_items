# Generated by Django 2.0 on 2018-12-17 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0013_auto_20181203_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='book_format',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='items.BookFormat'),
        ),
        migrations.AlterField(
            model_name='item',
            name='number_of_volumes',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Number of volumes, as listed in the catalogue'),
        ),
    ]
