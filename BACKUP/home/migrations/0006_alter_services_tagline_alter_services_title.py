# Generated by Django 4.1.5 on 2023-01-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_services_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='tagline',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
