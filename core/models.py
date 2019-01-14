from django.db import models


class TimeLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    activated_at = models.DateTimeField(null=True, blank=True, editable=False)
    deactivated_at = models.DateTimeField(null=True, blank=True, editable=False)
    published_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class Status(models.Model):
    is_active = models.BooleanField(default=True, null=False, blank=False)
    is_published = models.BooleanField(default=True, null=False, blank=False)
    is_deleted = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        abstract = True
