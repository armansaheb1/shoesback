# Generated by Django 4.0.1 on 2022-01-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_material_bumpmap'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='bumpmap',
            field=models.ImageField(null=True, upload_to='bumpmaps'),
        ),
    ]