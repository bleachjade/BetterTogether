# Generated by Django 2.2.5 on 2019-11-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetterTogetherApp', '0002_auto_20191107_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharefood',
            name='full',
        ),
        migrations.RemoveField(
            model_name='sharepromotion',
            name='full',
        ),
        migrations.RemoveField(
            model_name='shareride',
            name='full',
        ),
        migrations.AddField(
            model_name='sharefood',
            name='vacant',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sharepromotion',
            name='vacant',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shareride',
            name='vacant',
            field=models.BooleanField(default=True),
        ),
    ]
