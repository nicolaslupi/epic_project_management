# Generated by Django 3.1.7 on 2021-09-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0028_something'),
    ]

    operations = [
        migrations.AlterField(
            model_name='something',
            name='data',
            field=models.JSONField(db_index=True),
        ),
    ]
