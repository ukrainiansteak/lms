# Generated by Django 3.2.11 on 2022-05-10 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_alter_group_headman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='date_start',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
