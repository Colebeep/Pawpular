# Generated by Django 2.0.2 on 2018-04-05 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawpular', '0025_user_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='users',
            new_name='AccountPointer',
        ),
    ]
