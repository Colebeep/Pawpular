# Generated by Django 2.0.3 on 2018-03-28 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pawpular', '0023_auto_20180327_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pawpular.User'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pawpular.User'),
        ),
    ]