# Generated by Django 4.0.1 on 2022-01-24 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_material_bumpmap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='bumpmap',
        ),
    ]
