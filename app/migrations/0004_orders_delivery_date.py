# Generated by Django 2.2.17 on 2020-12-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201226_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='delivery_date',
            field=models.CharField(default=1983, max_length=30),
            preserve_default=False,
        ),
    ]
