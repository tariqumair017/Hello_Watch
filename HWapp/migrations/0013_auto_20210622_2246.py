# Generated by Django 3.2.4 on 2021-06-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HWapp', '0012_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
