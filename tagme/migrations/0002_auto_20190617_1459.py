# Generated by Django 2.0.13 on 2019-06-17 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagme', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'permissions': [('view_entities_with_this_tag', 'Can view entities with this tag')]},
        ),
        migrations.AlterModelOptions(
            name='taggedentity',
            options={'verbose_name_plural': 'TaggedEntities'},
        ),
    ]
