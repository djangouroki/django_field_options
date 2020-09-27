# Generated by Django 3.1 on 2020-09-27 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200912_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='fk self'),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, default='my default text', verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='url'),
        ),
    ]
