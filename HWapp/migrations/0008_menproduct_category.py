# Generated by Django 3.2.4 on 2021-06-16 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HWapp', '0007_auto_20210616_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='menproduct',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HWapp.category'),
        ),
    ]
