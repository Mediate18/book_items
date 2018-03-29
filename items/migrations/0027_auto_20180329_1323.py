# Generated by Django 2.0 on 2018-03-29 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptions', '0001_initial'),
        ('persons', '0001_initial'),
        ('items', '0026_work_viaf_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(verbose_name='Year of publication')),
                ('year_tag', models.CharField(max_length=128, verbose_name='Year of publication tag')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, verbose_name='The text of the class')),
            ],
        ),
        migrations.CreateModel(
            name='WorkAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='WorkSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Subject')),
            ],
        ),
        migrations.RemoveField(
            model_name='bindingmaterialdetailsequivalent',
            name='binding_material_details',
        ),
        migrations.RemoveField(
            model_name='bookformatequivalent',
            name='book_format',
        ),
        migrations.RemoveField(
            model_name='placeequivalent',
            name='place',
        ),
        migrations.DeleteModel(
            name='PlaceType',
        ),
        migrations.RemoveField(
            model_name='publisherequivalent',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='catalogue',
            name='source',
        ),
        migrations.RemoveField(
            model_name='item',
            name='date_of_publication',
        ),
        migrations.RemoveField(
            model_name='item',
            name='date_of_publication_tag',
        ),
        migrations.RemoveField(
            model_name='item',
            name='place_of_publication',
        ),
        migrations.RemoveField(
            model_name='item',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='work',
            name='text',
        ),
        migrations.AddField(
            model_name='catalogue',
            name='transcription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transcriptions.Transcription'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='persons.Person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='title',
            field=models.TextField(default='', verbose_name='Title of a work'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='collection',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.Place'),
        ),
        migrations.AlterField(
            model_name='personcataloguerelation',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='personcollectionrelation',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='personitemrelation',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='work',
            name='viaf_id',
            field=models.CharField(max_length=32, verbose_name='VIAF ID of a work'),
        ),
        migrations.DeleteModel(
            name='BindingMaterialDetailsEquivalent',
        ),
        migrations.DeleteModel(
            name='BookFormatEquivalent',
        ),
        migrations.DeleteModel(
            name='CatalogueSource',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='PlaceEquivalent',
        ),
        migrations.DeleteModel(
            name='PublisherEquivalent',
        ),
        migrations.AddField(
            model_name='worksubject',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Work'),
        ),
        migrations.AddField(
            model_name='workauthor',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='persons.Person'),
        ),
        migrations.AddField(
            model_name='workauthor',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='items.Work'),
        ),
        migrations.AddField(
            model_name='publication',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publications', to='items.Item'),
        ),
        migrations.AddField(
            model_name='publication',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persons.Place'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='publication',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.Publication'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='name',
        ),
        migrations.AlterUniqueTogether(
            name='publisher',
            unique_together={('publisher', 'publication')},
        ),
        migrations.AlterUniqueTogether(
            name='workauthor',
            unique_together={('work', 'author')},
        ),
    ]
