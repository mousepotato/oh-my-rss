# Generated by Django 2.2.9 on 2020-03-08 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.TextField(blank=True, default='', null=True, verbose_name='词频'),
        ),
    ]