# Generated by Django 4.1.5 on 2023-01-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuscontent',
            name='information',
            field=models.CharField(max_length=120),
        ),
    ]
