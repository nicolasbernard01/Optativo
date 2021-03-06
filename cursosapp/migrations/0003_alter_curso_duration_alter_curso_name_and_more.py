# Generated by Django 4.0.5 on 2022-06-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursosapp', '0002_rename_time_evento_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='duration',
            field=models.CharField(max_length=10, verbose_name='duration'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='name',
            field=models.CharField(max_length=20, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='price',
            field=models.IntegerField(verbose_name='price $'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='profesor',
            field=models.CharField(max_length=20, verbose_name='profesor'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='city',
            field=models.CharField(max_length=20, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='date',
            field=models.CharField(max_length=20, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='name',
            field=models.CharField(max_length=20, verbose_name='name'),
        ),
    ]
