# Generated by Django 4.0.1 on 2022-01-26 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_itemmaterials_part'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemmaterials',
            old_name='item',
            new_name='material',
        ),
    ]