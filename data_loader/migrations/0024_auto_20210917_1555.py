# Generated by Django 3.1.7 on 2021-09-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0023_auto_20210917_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='mail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='web',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]