# Generated by Django 4.1.5 on 2023-02-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_photos/default.png', null=True, upload_to='profile_photos/'),
        ),
    ]
