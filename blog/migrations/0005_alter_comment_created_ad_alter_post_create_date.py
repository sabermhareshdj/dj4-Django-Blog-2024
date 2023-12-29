# Generated by Django 5.0 on 2023-12-29 05:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_create_date_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_ad',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
