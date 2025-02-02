# Generated by Django 5.1.4 on 2025-01-14 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False, unique=True)),
                ('campaign', models.CharField(max_length=100)),
                ('received_date', models.DateField()),
                ('task', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Задания',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('campaign', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('operator', models.CharField(blank=True, max_length=100, null=True)),
                ('processed', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('base', models.CharField(blank=True, max_length=300, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('success', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Звонок',
                'verbose_name_plural': 'Звонок',
            },
        ),
    ]
