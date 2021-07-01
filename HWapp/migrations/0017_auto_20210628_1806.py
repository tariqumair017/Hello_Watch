# Generated by Django 3.2.4 on 2021-06-28 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HWapp', '0016_auto_20210625_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('Order_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Delivered', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Order_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HWapp.request'),
            preserve_default=False,
        ),
    ]