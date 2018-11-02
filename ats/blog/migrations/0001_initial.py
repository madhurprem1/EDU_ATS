# Generated by Django 2.0.7 on 2018-11-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('publish_date', models.DateTimeField(verbose_name='published date')),
                ('gPlus', models.IntegerField()),
            ],
        ),
    ]
