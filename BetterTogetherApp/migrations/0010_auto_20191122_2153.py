# Generated by Django 2.2.7 on 2019-11-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetterTogetherApp', '0009_auto_20191122_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareride',
            name='date_time',
            field=models.DateTimeField(default='2019-11-22 21:53:00', verbose_name='Date and Time'),
        ),
    ]
