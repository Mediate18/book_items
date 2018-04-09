from django.contrib import admin
from .models import *

# TODO The next bit should be in a more global place, but I could not find one (Micha, 2018-04-06)
from django.contrib.auth.models import Permission
admin.site.register(Permission)


@admin.register(MaterialDetails)
class BindingMaterialDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(BookFormat)
class BookFormatAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ['work__text']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonItemRelation)
class PersonItemRelationAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonItemRelationRole)
class PersonItemRelationRoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkAuthor)
class WorkAuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkSubject)
class WorkSubjectAdmin(admin.ModelAdmin):
    pass


