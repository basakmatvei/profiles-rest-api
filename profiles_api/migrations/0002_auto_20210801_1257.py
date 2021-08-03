# Generated by Django 2.2 on 2021-08-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directory',
            options={'verbose_name': 'Справочник', 'verbose_name_plural': 'Справочники'},
        ),
        migrations.AlterModelOptions(
            name='directoryitem',
            options={'verbose_name': 'Элемент', 'verbose_name_plural': 'Элементы'},
        ),
        migrations.AlterField(
            model_name='directory',
            name='description',
            field=models.TextField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='short_name',
            field=models.CharField(max_length=255, verbose_name='Короткое наименование'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='start_date',
            field=models.DateField(verbose_name='Дата начала действия справочника этой версии'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='version',
            field=models.CharField(max_length=255, verbose_name='Версия'),
        ),
        migrations.AlterField(
            model_name='directoryitem',
            name='element_code',
            field=models.CharField(max_length=255, verbose_name='Код элемента'),
        ),
        migrations.AlterField(
            model_name='directoryitem',
            name='value',
            field=models.CharField(max_length=255, verbose_name='Значение элемента'),
        ),
    ]
