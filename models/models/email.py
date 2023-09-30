from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Email(models.Model):
    label = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,default=1)
    object_id = models.PositiveIntegerField(null=True)
    emailable = GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        return self.email
   