from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("patients", views.patients, name="patients"),
    path("patients/<int:patient_id>/", views.patient, name="patient"),
    path("patients/search/<str:q>", views.search, name="search"),
]