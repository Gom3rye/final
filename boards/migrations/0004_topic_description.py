# Generated by Django 3.2.9 on 2021-12-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_topic_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(default='', max_length=4000),
        ),
    ]
