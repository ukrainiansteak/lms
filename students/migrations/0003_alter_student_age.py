# Generated by Django 3.2.11 on 2022-01-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]
