# Generated by Django 2.2.5 on 2019-09-10 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='res', max_length=255),
            preserve_default=False,
        ),
    ]