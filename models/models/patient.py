from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from .phone_number import PhoneNumber
from .email import Email
from .address import Address
from enum import Enum

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

class Patient(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('Date of birth')
    gender = models.CharField(max_length=200,choices=[(gender.value, gender.name) for gender in Gender])
    addresses = GenericRelation(Address,related_query_name='addressable')
    phone_numbers = GenericRelation(PhoneNumber,related_query_name='patients')
    emails = GenericRelation(Email,related_query_name='patients')
    registered_at = models.DateTimeField('Registration date', default=timezone.now)
    def __str__(self):
        return self.name + " " + self.last_name
    def age(self):
        return timezone.now().year - self.birth_date.year
    def is_adult(self):
        return self.age() >= 18
