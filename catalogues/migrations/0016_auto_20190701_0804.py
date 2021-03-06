# Generated by Django 2.0.13 on 2019-07-01 08:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0011_auto_20190429_1317'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogues', '0015_auto_20190701_0758'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CataloguePublicationPlace',
            new_name='CataloguePlaceRelation',
        ),
        migrations.RenameModel(
            old_name='HistoricalCataloguePublicationPlace',
            new_name='HistoricalCataloguePlaceRelation',
        ),
        migrations.AlterModelOptions(
            name='historicalcatalogueplacerelation',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical catalogue place relation'},
        ),
    ]
