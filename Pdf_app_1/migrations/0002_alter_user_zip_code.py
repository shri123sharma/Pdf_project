# Generated by Django 4.1.5 on 2023-01-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pdf_app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='zip_code',
            field=models.CharField(default='43701', max_length=8),
        ),
    ]
