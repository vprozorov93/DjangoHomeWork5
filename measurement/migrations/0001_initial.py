# Generated by Django 4.0.4 on 2022-05-11 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Датчик',
                'verbose_name_plural': 'Датчики',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('temperature', models.FloatField()),
                ('created_at', models.DateField()),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor')),
            ],
            options={
                'verbose_name': 'Показания',
                'verbose_name_plural': 'Показание',
            },
        ),
    ]
