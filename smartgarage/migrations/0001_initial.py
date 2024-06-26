# Generated by Django 5.0 on 2023-12-24 04:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=254)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=70)),
                ('contantnum', models.IntegerField()),
                ('price', models.FloatField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('totalslots', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=254)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sart_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('reservation_cost', models.FloatField(blank=True, null=True)),
                ('garage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartgarage.garage')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartgarage.user')),
            ],
        ),
    ]
