# Generated by Django 4.1.4 on 2023-01-26 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photos',
            options={'ordering': ('name',), 'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
    ]