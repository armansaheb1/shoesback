# Generated by Django 4.0.1 on 2022-01-26 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_itemmaterials'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmaterials',
            name='part',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.part'),
            preserve_default=False,
        ),
    ]
