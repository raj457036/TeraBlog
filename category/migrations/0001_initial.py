# Generated by Django 2.2.5 on 2019-09-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0006_post_series'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Category Name')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ManyToManyField(related_name='category', to='post.Post')),
            ],
        ),
    ]
