# Generated by Django 2.0 on 2018-04-05 13:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transcriptions', '0001_initial'),
        ('persons', '0002_auto_20180329_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('short_title', models.CharField(max_length=128, null=True, verbose_name='Short title')),
                ('full_title', models.TextField(null=True, verbose_name='Full title')),
                ('preface_and_paratexts', models.TextField(null=True, verbose_name='Preface or prefatory / concluding text')),
                ('year_of_publication', models.IntegerField(null=True, verbose_name='Year of publication')),
                ('terminus_post_quem', models.BooleanField(default=False, verbose_name='Terminus post quem')),
                ('notes', models.TextField(null=True, verbose_name='Notes for the Mediate project')),
                ('bibliography', models.TextField(null=True, verbose_name='Bibliography')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogueHeldBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogues.Catalogue')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogueType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Name of the catalogue type')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogues.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='The name of the library/institute')),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('bookseller_category_books', models.TextField(verbose_name='Heading / category used to describe books')),
                ('bookseller_category_non_books', models.TextField(verbose_name='Heading / category for other, non-book items')),
                ('number_in_catalogue', models.CharField(max_length=128, verbose_name='Number of items as listed in catalogue')),
                ('item_as_listed_in_catalogue', models.TextField(verbose_name='Full item description, exactly as in the catalogue')),
                ('catalogue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogues.Catalogue')),
            ],
        ),
        migrations.CreateModel(
            name='PersonCatalogueRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogues.Catalogue')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonCatalogueRelationRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Role name for a person-catalogue relation')),
            ],
        ),
        migrations.CreateModel(
            name='PersonCollectionRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogues.Collection')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person')),
            ],
        ),
        migrations.AddField(
            model_name='personcataloguerelation',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogues.PersonCatalogueRelationRole'),
        ),
        migrations.AddField(
            model_name='catalogueheldby',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogues.Library'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogues.Collection'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='transcription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transcriptions.Transcription'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogues.CatalogueType'),
        ),
        migrations.AlterUniqueTogether(
            name='personcollectionrelation',
            unique_together={('person', 'collection')},
        ),
    ]