# Generated by Django 2.2.4 on 2021-02-09 10:30

from django.db import migrations


def set_building_type(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        result = flat.construction_year >= 2015
        flat.new_building = result
        flat.save()
       

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(set_building_type),
    ]
