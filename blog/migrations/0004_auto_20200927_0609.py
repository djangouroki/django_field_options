# Generated by Django 3.1 on 2020-09-27 06:09

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200927_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, db_column='some_name', max_length=150, null=True, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, default=blog.models.get_default_text, verbose_name='text'),
        ),
    ]
