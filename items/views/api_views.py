from rest_framework import viewsets
from items.serializers import *


class BindingMaterialDetailsViewSet(viewsets.ModelViewSet):
    queryset = BindingMaterialDetails.objects.all()
    serializer_class = BindingMaterialDetailsSerializer


class BindingMaterialDetailsEquivalentViewSet(viewsets.ModelViewSet):
    queryset = BindingMaterialDetailsEquivalent.objects.all()
    serializer_class = BindingMaterialDetailsEquivalentSerializer


class BookFormatViewSet(viewsets.ModelViewSet):
    queryset = BookFormat.objects.all()
    serializer_class = BookFormatSerializer


class BookFormatEquivalentViewSet(viewsets.ModelViewSet):
    queryset = BookFormatEquivalent.objects.all()
    serializer_class = BookFormatEquivalentSerializer


class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer


class CatalogueViewSet(viewsets.ModelViewSet):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer


class CatalogueItemViewSet(viewsets.ModelViewSet):
    queryset = CatalogueItem.objects.all()
    serializer_class = CatalogueItemSerializer


class CatalogueTypeViewSet(viewsets.ModelViewSet):
    queryset = CatalogueType.objects.all()
    serializer_class = CatalogueTypeSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonBookItemRelationViewSet(viewsets.ModelViewSet):
    queryset = PersonBookItemRelation.objects.all()
    serializer_class = PersonBookItemRelationSerializer


class PersonBookItemRelationTypeViewSet(viewsets.ModelViewSet):
    queryset = PersonBookItemRelationType.objects.all()
    serializer_class = PersonBookItemRelationTypeSerializer


class PersonCatalogueRelationViewSet(viewsets.ModelViewSet):
    queryset = PersonCatalogueRelation.objects.all()
    serializer_class = PersonCatalogueRelationSerializer


class PersonCatalogueRelationTypeViewSet(viewsets.ModelViewSet):
    queryset = PersonCatalogueRelationType.objects.all()
    serializer_class = PersonCatalogueRelationTypeSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceEquivalentViewSet(viewsets.ModelViewSet):
    queryset = PlaceEquivalent.objects.all()
    serializer_class = PlaceEquivalentSerializer


class PlaceTypeViewSet(viewsets.ModelViewSet):
    queryset = PlaceType.objects.all()
    serializer_class = PlaceTypeSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherEquivalentViewSet(viewsets.ModelViewSet):
    queryset = PublisherEquivalent.objects.all()
    serializer_class = PublisherEquivalentSerializer


class TitleWorkViewSet(viewsets.ModelViewSet):
    queryset = TitleWork.objects.all()
    serializer_class = TitleWorkSerializer
