# Generated by Django 3.1.7 on 2021-10-12 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarios', models.CharField(blank=True, max_length=200, null=True)),
                ('unidades', models.IntegerField()),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_loader.item')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_loader.project')),
                ('retirado_por', models.ManyToManyField(to='data_loader.Person')),
                ('system', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_loader.system')),
            ],
        ),
    ]
