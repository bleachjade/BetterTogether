# Generated by Django 2.2.5 on 2019-12-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetterTogetherApp', '0015_auto_20191215_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharefood',
            name='date_time',
            field=models.TextField(default='2019-12-15 21:34:07', verbose_name='Date and Time'),
        ),
        migrations.AlterField(
            model_name='sharepromotion',
            name='date_time',
            field=models.TextField(default='2019-12-15 21:34:07', verbose_name='Date and Time'),
        ),
        migrations.AlterField(
            model_name='shareride',
            name='date_time',
            field=models.TextField(default='2019-12-15 21:34:07', verbose_name='Date and Time'),
        ),
    ]
