# Generated by Django 4.1.5 on 2023-02-15 05:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
