# Generated by Django 4.1.5 on 2023-01-23 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_services_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='services',
            table='home_services',
        ),
    ]