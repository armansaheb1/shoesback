# Generated by Django 4.0.1 on 2022-01-26 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_itemmaterials_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmaterials',
            name='material',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.material'),
            preserve_default=False,
        ),
    ]
