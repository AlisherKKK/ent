# Generated by Django 3.1.5 on 2021-01-13 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0007_auto_20210113_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trial',
            name='trial_sub_id',
        ),
    ]
