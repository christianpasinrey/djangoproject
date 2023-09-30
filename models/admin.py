from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models.patient import Patient
from .models.phone_number import PhoneNumber
from .models.email import Email
from .models.address import Address


# Make the Poll Patient has a fieldset to add Addresses, Emails and PhoneNumbers
class AddressInline(GenericTabularInline):
    model = Address
    extra = 1
class EmailInline(GenericTabularInline):
    model = Email
    extra = 1
class PhoneNumberInline(GenericTabularInline):
    model = PhoneNumber
    extra = 1

class PatientAdmin(admin.ModelAdmin):
    inlines = [AddressInline,EmailInline,PhoneNumberInline]
    exclude = ('registered_at',)
""" hide registration date from admin """
admin.site.register(Patient, PatientAdmin)



