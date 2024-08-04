# Generated by Django 4.2.3 on 2024-08-04 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(limit_value=6, message='Password must be at least 6 characters.')]),
        ),
    ]
