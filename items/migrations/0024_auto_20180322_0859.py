# Generated by Django 2.0 on 2018-03-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0023_auto_20180322_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='terminus_post_quem',
            field=models.BooleanField(default=False, verbose_name='Terminus post quem'),
        ),
    ]
