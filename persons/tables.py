import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from django.utils.html import format_html
from .models import *
from mediate.columns import ActionColumn
from catalogues.models import PersonCatalogueRelation, Catalogue
from items.models import PersonItemRelation, Manifestation
from django.utils.translation import ugettext_lazy as _


# Person table
class PersonTable(tables.Table):
    uuid = ActionColumn('person_detail', 'change_person', 'delete_person', orderable=False)
    catalogues = tables.Column(empty_values=())
    roles = tables.Column(empty_values=())
    viaf_id = tables.Column(empty_values=())

    class Meta:
        model = Person
        attrs = {'class': 'table table-sortable'}
        sequence = [
            'short_name',
            'first_names',
            'surname',
            'sex',
            'roles',
            'city_of_birth',
            'date_of_birth',
            'city_of_death',
            'date_of_death',
            'catalogues',
            'viaf_id',
            'uuid'
        ]

    def render_catalogues(self, record):
        person_catalogue_relations = PersonCatalogueRelation.objects.filter(person=record, role__name="owner")
        relation_groups = []
        for role in set([relation.role for relation in person_catalogue_relations]):
            role_relations = person_catalogue_relations.filter(role=role)
            catalogues = []
            for relation in role_relations:
                catalogue = relation.catalogue
                title = catalogue.short_title
                catalogue_entry = "<a href='{}'>{}</a>".format(reverse_lazy('catalogue_detail', args=[catalogue.pk]), title)
                catalogues.append(catalogue_entry)

            relation_groups.append(", ".join(catalogues))
        return format_html("<br/> ".join(relation_groups))

    def render_roles(self, record):
        roles_dict = {}

        # Catalogues
        catalogue_roles = list(PersonCatalogueRelation.objects.filter(person=record).distinct()
                               .values_list('role__name', flat=True))
        if catalogue_roles:
            roles_dict['catalogues'] = catalogue_roles

        # Items
        item_roles = list(PersonItemRelation.objects.filter(person=record).distinct()
                          .values_list('role__name', flat=True))
        if item_roles:
            roles_dict['items'] = item_roles

        # Manifestations
        manifestations_count = record.publisher_set.count()
        if manifestations_count:
            roles_dict['manifestation'] = ['publisher']

        # Works
        work_count = record.works.count()
        if work_count:
            roles_dict['works'] = ['author']

        text = "<br/>".join(["{}: {}".format(k.capitalize(), ", ".join(v)) for k, v in roles_dict.items()])
        return format_html('<a href="{}">{}</a>'.format(reverse_lazy('person_detail', args=[record.pk]), text))

    def render_viaf_id(self, value):
        if value:
            return format_html('<a target="blank" href="{}">{}</a>'.format(
                value, value
            ))
        else:
            return format_html('-')


# PersonPersonRelation table
class PersonPersonRelationTable(tables.Table):
    uuid = ActionColumn('personpersonrelation_detail', 'change_personpersonrelation', 'delete_personpersonrelation',
                        orderable=False)

    class Meta:
        model = PersonPersonRelation
        attrs = {'class': 'table table-sortable'}
        sequence = [
            'first_person',
            'second_person',
            'type',
            'start_year',
            'end_year',
            'uuid'
        ]


# PersonPersonRelationType table
class PersonPersonRelationTypeTable(tables.Table):
    uuid = ActionColumn('personpersonrelationtype_detail', 'change_personpersonrelationtype',
                        'delete_personpersonrelationtype', orderable=False)

    class Meta:
        model = PersonPersonRelationType
        attrs = {'class': 'table table-sortable'}
        sequence = [
            'name',
            'directed',
            'uuid'
        ]


# PersonProfession table
class PersonProfessionTable(tables.Table):
    uuid = ActionColumn('personprofession_detail', 'change_personprofession', 'delete_personprofession',
                        orderable=False)

    class Meta:
        model = PersonProfession
        attrs = {'class': 'table table-sortable'}
        sequence = [
            'person',
            'profession',
            'uuid'
        ]


# Country table
class CountryTable(tables.Table):
    uuid = ActionColumn('country_detail', 'change_country', 'delete_country',
                        orderable=False)

    class Meta:
        model = Country
        attrs = {'class': 'table table-sortable'}
        sequence = [
            'name',
            'uuid'
        ]


# Place table
class PlaceTable(tables.Table):
    uuid = ActionColumn('place_detail', 'change_place', 'delete_place',
                        orderable=False)

    class Meta:
        model = Place
        attrs = {'class': 'table table-sortable'}
        sequence = [
            'name',
            'cerl_id',
            'country',
            'uuid'
        ]


# Place links table
class PlaceLinksTable(tables.Table):
    uuid = ActionColumn('place_detail', 'change_place', 'delete_place',
                        orderable=False)
    catalogues = tables.Column(empty_values=(), verbose_name="Catalogues",
                        orderable=False)
    manifestations = tables.Column(empty_values=(), verbose_name="Manifestations",
                        orderable=False)
    people_born = tables.Column(empty_values=(), verbose_name="People born",
                        orderable=False)
    people_died = tables.Column(empty_values=(), verbose_name="People died",
                        orderable=False)
    residences = tables.Column(empty_values=(), verbose_name="People inhabiting",
                        orderable=False)

    class Meta:
        model = Place
        attrs = {'class': 'table table-sortable'}
        fields = [
            'name',
            'catalogues',
            'manifestations',
            'people_born',
            'people_died',
            'residences',
            'uuid'
        ]

    def render_catalogues(self, record):
        catalogues = Catalogue.objects.filter(publication_places__place=record)
        return format_html(", ".join(
            ['<a href="{}">{}</a>'.format(reverse_lazy('catalogue_detail', args=[catalogue.pk]), catalogue)
                for catalogue in catalogues]
        ))

    def render_manifestations(self, record):
        manifestations = Manifestation.objects.filter(place=record)
        return format_html(", ".join(
            ['<a href="{}">{}</a>'.format(reverse_lazy('manifestation_detail', args=[manifestation.pk]),
                                          manifestation)
                for manifestation in manifestations]
        ))

    def render_people_born(self, record):
        persons = Person.objects.filter(city_of_birth=record)
        return format_html(", ".join(
            ['<a href="{}">{}</a>'.format(reverse_lazy('person_detail', args=[person.pk]),
                                          person)
                for person in persons]
        ))

    def render_people_died(self, record):
        persons = Person.objects.filter(city_of_death=record)
        return format_html(", ".join(
            ['<a href="{}">{}</a>'.format(reverse_lazy('person_detail', args=[person.pk]),
                                          person)
                for person in persons]
        ))

    def render_residences(self, record):
        persons = Person.objects.filter(residence__place=record)
        return format_html(", ".join(
            ['<a href="{}">{}</a>'.format(reverse_lazy('person_detail', args=[person.pk]),
                                          person)
                for person in persons]
        ))


# Profession table
class ProfessionTable(tables.Table):
    uuid = ActionColumn('profession_detail', 'change_profession', 'delete_profession', orderable=False)

    class Meta:
        model = Profession
        attrs = {'class': 'table table-sortable'}
        sequence = [
            'name',
            'description',
            'uuid'
        ]


# Religion table
class ReligionTable(tables.Table):
    uuid = ActionColumn('religion_detail', 'change_religion', 'delete_religion', orderable=False)

    class Meta:
        model = Religion
        attrs = {'class': 'table table-sortable'}
        sequence = [
            'name',
            'description',
            'uuid'
        ]


# ReligiousAffiliation table
class ReligiousAffiliationTable(tables.Table):
    uuid = ActionColumn('religiousaffiliation_detail', 'change_religiousaffiliation', 'delete_religiousaffiliation',
                        orderable=False)

    class Meta:
        model = ReligiousAffiliation
        attrs = {'class': 'table table-sortable'}
        sequence = [
            'person',
            'religion',
            'uuid'
        ]


# Residence table
class ResidenceTable(tables.Table):
    uuid = ActionColumn('residence_detail', 'change_residence', 'delete_residence',
                        orderable=False)

    class Meta:
        model = Residence
        attrs = {'class': 'table table-sortable'}
        sequence = [
            'person',
            'place',
            'start_year',
            'end_year',
            'uuid'
        ]


