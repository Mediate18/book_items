# Generated by Django 2.0 on 2018-02-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0020_auto_20180219_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personcataloguerelationrole',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Role name for a person-catalogue relation'),
        ),
    ]