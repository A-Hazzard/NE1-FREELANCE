# Generated by Django 4.1.5 on 2023-01-24 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searchResults', '0007_jobcategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searchResults.jobcategory'),
        ),
    ]
