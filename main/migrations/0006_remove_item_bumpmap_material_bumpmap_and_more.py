# Generated by Django 4.0.1 on 2022-01-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_part_model_alter_pattern_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='bumpmap',
        ),
        migrations.AddField(
            model_name='material',
            name='bumpmap',
            field=models.ImageField(default=None, upload_to='bumpmaps'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pattern',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]