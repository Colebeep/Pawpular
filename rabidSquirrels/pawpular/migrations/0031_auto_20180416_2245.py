# Generated by Django 2.0.3 on 2018-04-17 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawpular', '0030_auto_20180416_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='signUpDate',
        ),
    ]
