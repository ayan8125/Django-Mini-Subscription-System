# Generated by Django 2.2.5 on 2020-07-21 11:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subcriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='priceid',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='current_end_At',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 20, 11, 27, 43, 306576, tzinfo=utc)),
        ),
    ]
