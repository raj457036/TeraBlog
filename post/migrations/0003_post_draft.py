# Generated by Django 2.2.5 on 2019-09-10 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190910_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Is Draft'),
        ),
    ]