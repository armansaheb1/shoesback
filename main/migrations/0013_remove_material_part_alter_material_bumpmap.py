# Generated by Django 4.0.1 on 2022-01-26 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_item_itemmaterials_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='part',
        ),
        migrations.AlterField(
            model_name='material',
            name='bumpmap',
            field=models.ImageField(blank=True, null=True, upload_to='bumpmaps'),
        ),
    ]