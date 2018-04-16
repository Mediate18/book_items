import django_filters
from .models import *


# BookFormat filter
class BookFormatFilter(django_filters.FilterSet):
    class Meta:
        model = BookFormat
        fields = "__all__"


# Item filter
class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = "__all__"


# ItemAuthor filter
class ItemAuthorFilter(django_filters.FilterSet):
    class Meta:
        model = ItemAuthor
        fields = "__all__"


# ItemBookFormatRelation filter
class ItemBookFormatRelationFilter(django_filters.FilterSet):
    class Meta:
        model = ItemBookFormatRelation
        fields = "__all__"


# ItemItemTypeRelation filter
class ItemItemTypeRelationFilter(django_filters.FilterSet):
    class Meta:
        model = ItemItemTypeRelation
        fields = "__all__"


# ItemLanguageRelation filter
class ItemLanguageRelationFilter(django_filters.FilterSet):
    class Meta:
        model = ItemLanguageRelation
        fields = "__all__"


# ItemMaterialDetailsRelation filter
class ItemMaterialDetailsRelationFilter(django_filters.FilterSet):
    class Meta:
        model = ItemMaterialDetailsRelation
        fields = "__all__"


# ItemType filter
class ItemTypeFilter(django_filters.FilterSet):
    class Meta:
        model = ItemType
        fields = "__all__"


# ItemWorkRelation filter
class ItemWorkRelationFilter(django_filters.FilterSet):
    class Meta:
        model = ItemWorkRelation
        fields = "__all__"


# Language filter
class LanguageFilter(django_filters.FilterSet):
    class Meta:
        model = Language
        fields = "__all__"


# MaterialDetails filter
class MaterialDetailsFilter(django_filters.FilterSet):
    class Meta:
        model = MaterialDetails
        fields = "__all__"


# PersonItemRelation filter
class PersonItemRelationFilter(django_filters.FilterSet):
    class Meta:
        model = PersonItemRelation
        fields = "__all__"


# PersonItemRelationRole filter
class PersonItemRelationRoleFilter(django_filters.FilterSet):
    class Meta:
        model = PersonItemRelationRole
        fields = "__all__"


# Publication filter
class PublicationFilter(django_filters.FilterSet):
    class Meta:
        model = Publication
        fields = "__all__"


# Publisher filter
class PublisherFilter(django_filters.FilterSet):
    class Meta:
        model = Publisher
        fields = "__all__"


# Subject filter
class SubjectFilter(django_filters.FilterSet):
    class Meta:
        model = Subject
        fields = "__all__"


# Work filter
class WorkFilter(django_filters.FilterSet):
    class Meta:
        model = Work
        fields = "__all__"


# WorkAuthor filter
class WorkAuthorFilter(django_filters.FilterSet):
    class Meta:
        model = WorkAuthor
        fields = "__all__"


# WorkSubject filter
class WorkSubjectFilter(django_filters.FilterSet):
    class Meta:
        model = WorkSubject
        fields = "__all__"


