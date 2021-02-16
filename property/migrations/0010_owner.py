# Generated by Django 2.2.4 on 2021-02-09 14:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20210209_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО Владельца')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('pure_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца')),
                ('owned_apartments', models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
