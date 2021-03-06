from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

import uuid

from simplemoderation.tools import moderated


class SourceMaterial(models.Model):
    """
    Source material
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Source material name"), max_length=128)

    def __str__(self):
        return self.name


@moderated()
class Transcription(models.Model):
    """
    Transcription
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField(_("Creation date"), auto_now_add=True)
    source_material = models.ForeignKey(SourceMaterial, on_delete=models.PROTECT)
    curator = models.CharField(_("Curator"), max_length=128)

    def __str__(self):
        return _("{} as transcribed by {} ({})").format(self.source_material, self.author,
                                                      ", ".join([str(scan.scan) for scan in self.scans.all()]))

    def get_absolute_url(self):
        return reverse_lazy('transcription_detail', args=[str(self.uuid)])

class DocumentScan(models.Model):
    """
    Document scan
    """
    DOCUMENT_SCAN_FOLDER = 'document_scans'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transcription = models.ForeignKey(Transcription, on_delete=models.SET_NULL, null=True, related_name="scans")
    scan = models.FileField(upload_to=DOCUMENT_SCAN_FOLDER)


    def __str__(self):
        return self.scan.name

    def delete(self, using=None, keep_parents=False):
        # Prepare to move the scan file
        import os
        from django.conf import settings
        old_path = self.scan.path
        file_name = os.path.basename(old_path)
        new_folder = os.path.join(settings.MEDIA_ROOT, self.DOCUMENT_SCAN_FOLDER, 'deleted')
        os.makedirs(new_folder, exist_ok=True)
        new_path = os.path.join(new_folder, '{}_{}_{}'.format(self.__class__.__name__, self.uuid, file_name))

        # Delete the object
        super(DocumentScan, self).delete(using=using, keep_parents=keep_parents)

        # Move the scan file
        os.rename(old_path, new_path)


# Enable the simple-history registration:
from .history import *
