# Generated by Django 2.0 on 2018-02-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_auto_20180219_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personitemrelationrole',
            name='name',
            field=models.CharField(max_length=128, null=True, verbose_name='Role name for a person-item relation'),
        ),
    ]
