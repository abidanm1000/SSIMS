# Generated by Django 2.2.17 on 2020-12-28 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivery_date',
            field=models.DateField(),
        ),
    ]
