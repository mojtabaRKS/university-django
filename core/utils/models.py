from pydoc import describe
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """Base Model for customizing all models

    Args:
        models (Class): django model
    """

    active = models.BooleanField(default=True, help_text="instead of delete with just controll activation")

    created_at = models.DateTimeField(auto_now_add=True, help_text="time of object creation", editable=False)
    modeified_at = models.DateTimeField(auto_now=True, help_text="every time any objects have a change this item will be updated to")
    deleted_at = models.DateTimeField(help_text="deactivation time")

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True
