# Generated by Django 4.1.5 on 2023-01-24 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crud_pro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='langauage',
            new_name='developer_langauage',
        ),
        migrations.RenameField(
            model_name='developer',
            old_name='role',
            new_name='developer_roler',
        ),
        migrations.RenameField(
            model_name='developer',
            old_name='user',
            new_name='developer_user',
        ),
    ]
