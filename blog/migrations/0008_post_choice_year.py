# Generated by Django 3.1 on 2020-09-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200927_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='choice_year',
            field=models.PositiveSmallIntegerField(choices=[(2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013)], default=2009, verbose_name='year'),
            preserve_default=False,
        ),
    ]
