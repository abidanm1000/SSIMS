# Generated by Django 2.2.17 on 2020-12-28 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20201227_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='item_name',
            new_name='inventory_id',
        ),
    ]