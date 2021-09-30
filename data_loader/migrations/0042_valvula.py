# Generated by Django 3.1.7 on 2021-09-28 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0041_auto_20210928_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valvula',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data_loader.item')),
                ('material', models.CharField(blank=True, max_length=200, null=True)),
                ('pugladas', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'valvulas',
            },
            bases=('data_loader.item',),
        ),
    ]