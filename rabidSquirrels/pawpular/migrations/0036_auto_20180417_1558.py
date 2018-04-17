# Generated by Django 2.0.2 on 2018-04-17 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pawpular', '0035_auto_20180417_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedpost',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pawpular.Profile'),
        ),
        migrations.AlterField(
            model_name='mappost',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pawpular.Profile'),
        ),
        migrations.AlterField(
            model_name='servicepost',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pawpular.Profile'),
        ),
    ]