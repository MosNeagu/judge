# Generated by Django 3.0.8 on 2020-07-18 00:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='result',
            field=models.FileField(blank=True, default='media/media/output.txt', null=True, upload_to='media', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt'])]),
        ),
    ]
