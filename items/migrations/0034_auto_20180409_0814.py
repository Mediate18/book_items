# Generated by Django 2.0 on 2018-04-09 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0033_auto_20180409_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialdetails',
            name='description',
            field=models.CharField(max_length=128, null=True, verbose_name='Binding material details description'),
        ),
    ]
