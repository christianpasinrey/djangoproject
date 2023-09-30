from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Address(models.Model):
    street = models.CharField(max_length=200)
    number = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,default=1)
    object_id = models.PositiveIntegerField(null=True)
    addressable = GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        return self.street + " " + str(self.number) + ", " + self.city + ", " + self.state + ", " + self.country
