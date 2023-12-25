# Generated by Django 5.0 on 2023-12-25 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=30000)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2023, 12, 25, 7, 37, 48, 7192, tzinfo=datetime.timezone.utc))),
                ('draft', models.BooleanField(default=True)),
            ],
        ),
    ]
