# Generated by Django 4.0.1 on 2022-03-14 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='patina',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='patinad',
            field=models.BooleanField(default=False),
        ),
    ]