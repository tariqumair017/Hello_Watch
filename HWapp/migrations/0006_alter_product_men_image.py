# Generated by Django 3.2.4 on 2021-06-16 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HWapp', '0005_alter_product_men_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_men',
            name='image',
            field=models.ImageField(upload_to='img/%y'),
        ),
    ]
