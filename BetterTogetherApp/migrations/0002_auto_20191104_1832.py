# Generated by Django 2.2.5 on 2019-11-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetterTogetherApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharefood',
            name='host',
            field=models.CharField(default='', max_length=30, verbose_name="Host's Name"),
        ),
        migrations.AlterField(
            model_name='sharepromotion',
            name='host',
            field=models.CharField(default='', max_length=30, verbose_name="Host's Name"),
        ),
        migrations.AlterField(
            model_name='shareride',
            name='host',
            field=models.CharField(default='', max_length=30, verbose_name="Host's Name"),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=1, verbose_name='Gender (F or M)'),
        ),
    ]