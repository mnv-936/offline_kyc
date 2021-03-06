# Generated by Django 2.1.7 on 2020-06-27 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyc', '0003_auto_20200627_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='xxx', max_length=256),
        ),
        migrations.AddField(
            model_name='customer',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='xxx', max_length=256),
        ),
        migrations.AlterField(
            model_name='customer',
            name='xml',
            field=models.FileField(upload_to='xmls/'),
        ),
    ]
