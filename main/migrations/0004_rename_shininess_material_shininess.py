# Generated by Django 4.0.1 on 2022-01-19 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_item_part_item_alter_pattern_color_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='Shininess',
            new_name='shininess',
        ),
    ]