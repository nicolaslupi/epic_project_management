# Generated by Django 3.1.7 on 2021-11-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='part_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]