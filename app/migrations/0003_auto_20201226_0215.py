# Generated by Django 2.2.17 on 2020-12-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201226_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='item_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]