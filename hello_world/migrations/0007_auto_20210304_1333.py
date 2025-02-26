# Generated by Django 3.1.5 on 2021-03-04 10:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0006_auto_20210208_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 10, 33, 18, 509147, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 10, 33, 18, 508147, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='thread',
            name='unit',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hello_world.unit'),
        ),
    ]
