# Generated by Django 2.0 on 2018-09-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0008_auto_20180907_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='bookseller_category_non_books',
            field=models.TextField(blank=True, verbose_name='Heading / category for other, non-book items'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='page_in_catalogue',
            field=models.IntegerField(blank=True, null=True, verbose_name='Page in catalogue'),
        ),
    ]