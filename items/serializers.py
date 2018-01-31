from items.models import *
from rest_framework import serializers


class BindingMaterialDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BindingMaterialDetails
        fields = "__all__"


class BindingMaterialDetailsEquivalentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BindingMaterialDetailsEquivalent
        fields = "__all__"


class BookFormatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookFormat
        fields = "__all__"


class BookFormatEquivalentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookFormatEquivalent
        fields = "__all__"


class BookItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookItem
        fields = "__all__"


class CatalogueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalogue
        fields = "__all__"


class CatalogueItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogueItem
        fields = "__all__"


class CatalogueTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogueType
        fields = "__all__"


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class PersonBookItemRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonBookItemRelation
        fields = "__all__"


class PersonBookItemRelationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonBookItemRelationType
        fields = "__all__"


class PersonCatalogueRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonCatalogueRelation
        fields = "__all__"


class PersonCatalogueRelationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonCatalogueRelationType
        fields = "__all__"


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class PlaceEquivalentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaceEquivalent
        fields = "__all__"


class PlaceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaceType
        fields = "__all__"


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class PublisherEquivalentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublisherEquivalent
        fields = "__all__"


class TitleWorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TitleWork
        fields = "__all__"
