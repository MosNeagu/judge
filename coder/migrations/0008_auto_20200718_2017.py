# Generated by Django 3.0.8 on 2020-07-18 14:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0007_auto_20200718_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='result',
            field=models.FileField(blank=True, null=True, upload_to='media', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt'])]),
        ),
    ]
