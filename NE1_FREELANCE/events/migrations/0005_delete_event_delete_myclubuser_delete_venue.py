# Generated by Django 4.1.5 on 2023-01-31 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_manager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='MyClubUser',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
