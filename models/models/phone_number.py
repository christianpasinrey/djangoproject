from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class PhoneNumber(models.Model):
    label = models.CharField(max_length=200)
    number = models.IntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,default=1)
    object_id = models.PositiveIntegerField(null=True)
    phoneable = GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        return str(self.number)
  