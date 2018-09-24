# Generated by Django 2.0 on 2018-09-24 08:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0009_auto_20180907_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParisianCategory',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bookseller_category', models.TextField(verbose_name='Heading / category used to describe books')),
                ('catalogue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogues.Catalogue')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogues.Category')),
                ('parisian_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogues.ParisianCategory')),
            ],
        ),
    ]
