# Generated by Django 2.1.5 on 2019-02-17 01:18

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='graph',
            field=models.ImageField(null=True, upload_to='graph'),
        ),
        migrations.AddField(
            model_name='post',
            name='x',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AddField(
            model_name='post',
            name='y',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
