# Generated by Django 3.2.4 on 2021-06-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HWapp', '0010_auto_20210617_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='login_password',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_num',
            field=models.CharField(max_length=15),
        ),
    ]