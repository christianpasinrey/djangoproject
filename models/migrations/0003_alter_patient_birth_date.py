# Generated by Django 4.2.5 on 2023-09-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateTimeField(verbose_name='date of birth'),
        ),
    ]