# Generated by Django 2.2.4 on 2021-02-10 11:10

from django.db import migrations


def load_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats:
        owners = Owner.objects.filter(full_name=flat.owner)
        for owner in owners:
            filtered_flats = Flat.objects.filter(owner=owner.full_name)
            owner.owned_apartments.set(filtered_flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20210210_1159'),
    ]

    operations = [
        migrations.RunPython(load_flats)
    ]
