# Generated by Django 4.1.5 on 2023-01-24 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchResults', '0006_rename_categorie_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
