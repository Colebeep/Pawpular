# Generated by Django 2.0.3 on 2018-04-17 02:37

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('pawpular', '0029_auto_20180416_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('signUpDate', models.DateField()),
                ('lname', models.CharField(max_length=45)),
                ('fname', models.CharField(max_length=45)),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
                ('settings', models.CharField(choices=[('1', 'on'), ('0', 'off')], default='1', help_text='settings status status', max_length=1)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='feedPosts',
        ),
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mapPosts',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pets',
        ),
        migrations.RemoveField(
            model_name='user',
            name='servicePosts',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pawpular.Profile'),
        ),
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
            model_name='pet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pawpular.Profile'),
        ),
        migrations.AlterField(
            model_name='servicepost',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pawpular.Profile'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='feedPosts',
            field=models.ManyToManyField(blank=True, to='pawpular.FeedPost'),
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='pawpular.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='mapPosts',
            field=models.ManyToManyField(blank=True, to='pawpular.MapPost'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pets',
            field=models.ManyToManyField(blank=True, to='pawpular.Pet'),
        ),
        migrations.AddField(
            model_name='profile',
            name='servicePosts',
            field=models.ManyToManyField(blank=True, to='pawpular.ServicePost'),
        ),
    ]
