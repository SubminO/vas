# Generated by Django 2.2.2 on 2019-08-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0005_auto_20190819_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busmodel',
            name='techquality',
            field=models.IntegerField(choices=[(1, 'не находу'), (2, 'плохое'), (3, 'удовлетворительное'), (4, 'хорошее'), (5, 'отличное')], default=4, verbose_name='Техническое состояние'),
        ),
        migrations.AddIndex(
            model_name='busmodel',
            index=models.Index(fields=['uuid', 'name'], name='vehicles_uuid_70fb02_idx'),
        ),
        migrations.AlterModelTable(
            name='busmodel',
            table='vehicles',
        ),
    ]