# Generated by Django 2.2.2 on 2019-09-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0010_auto_20190916_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platformtype',
            name='name',
            field=models.CharField(help_text='Название типа остановки', max_length=100, verbose_name='Тип остановки'),
        ),
    ]
