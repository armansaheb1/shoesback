# Generated by Django 4.0.1 on 2022-01-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_shininess_material_shininess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='model',
            field=models.FileField(null=True, upload_to='models'),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='color',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='texture',
            field=models.ImageField(blank=True, null=True, upload_to='textures'),
        ),
    ]
