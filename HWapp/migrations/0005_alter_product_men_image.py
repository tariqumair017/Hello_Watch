# Generated by Django 3.2.4 on 2021-06-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HWapp', '0004_auto_20210616_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_men',
            name='image',
            field=models.ImageField(upload_to='men/%y'),
        ),
    ]
