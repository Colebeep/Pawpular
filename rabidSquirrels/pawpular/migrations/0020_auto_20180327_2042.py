# Generated by Django 2.0.3 on 2018-03-28 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawpular', '0019_auto_20180327_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedpost',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mappost',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='servicepost',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
