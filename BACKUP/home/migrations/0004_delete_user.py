# Generated by Django 4.1.5 on 2023-01-30 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_user_date_joined'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
