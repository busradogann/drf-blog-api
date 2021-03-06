# Generated by Django 3.0.4 on 2020-03-10 12:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200310_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 12, 45, 17, 204111, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='media',
            field=models.ImageField(default=datetime.datetime(2020, 3, 10, 12, 48, 32, 276084, tzinfo=utc), upload_to='media/post/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 12, 48, 42, 50460, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2020, 3, 10, 12, 48, 56, 198952, tzinfo=utc), editable=False, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
