# Generated by Django 3.1.5 on 2021-01-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_auto_20210112_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='pers_password',
            field=models.CharField(default=1, max_length=100, verbose_name='passwd'),
            preserve_default=False,
        ),
    ]
