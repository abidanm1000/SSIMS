# Generated by Django 2.2.17 on 2020-12-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='paid_status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
