# Generated by Django 5.1.4 on 2025-01-14 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oper_stat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='base',
            options={'verbose_name': 'База', 'verbose_name_plural': 'База'},
        ),
        migrations.AlterField(
            model_name='call',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='start_time',
            field=models.TimeField(),
        ),
        migrations.AlterModelTable(
            name='base',
            table='base',
        ),
        migrations.AlterModelTable(
            name='call',
            table='call',
        ),
    ]
