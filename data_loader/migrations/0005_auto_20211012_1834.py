# Generated by Django 3.1.7 on 2021-10-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0004_auto_20211012_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='in_stock',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='total_units',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]