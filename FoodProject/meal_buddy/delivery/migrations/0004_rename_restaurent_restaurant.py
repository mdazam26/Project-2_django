# Generated by Django 5.2 on 2025-04-28 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_rename_restaurent_name_restaurent_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurent',
            new_name='Restaurant',
        ),
    ]
