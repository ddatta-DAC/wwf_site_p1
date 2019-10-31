from django.conf import settings
from django.db import models


class Comment(models.Model):
    panjivarecordid = models.BigIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    comment = models.TextField()

    class Meta:
        abstract = True
        unique_together = ('user', 'panjivarecordid',)


class ChinaExportComment(Comment):
    pass


class ChinaImportComment(Comment):
    pass


class PeruExportComment(Comment):
    pass


class UsImportComment(Comment):
    pass


THUMBS_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('clear', 'Clear'),
)


class Thumbs(models.Model):
    panjivarecordid = models.BigIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    thumbs = models.CharField(
        max_length=5,
        choices=THUMBS_CHOICES,
        default="clear")

    class Meta:
        abstract = True
        unique_together = ('user', 'panjivarecordid',)


class ChinaExportThumbs(Thumbs):
    pass


class ChinaImportThumbs(Thumbs):
    pass


class PeruExportThumbs(Thumbs):
    pass


class UsImportThumbs(Thumbs):
    pass
