# Generated by Django 4.1.2 on 2023-11-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0004_articlecountview_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='оличество просмотров'),
        ),
    ]
