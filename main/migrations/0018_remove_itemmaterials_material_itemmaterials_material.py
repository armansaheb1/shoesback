# Generated by Django 4.0.1 on 2022-01-26 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_itemmaterials_material_itemmaterials_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmaterials',
            name='material',
        ),
        migrations.AddField(
            model_name='itemmaterials',
            name='material',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.material'),
            preserve_default=False,
        ),
    ]