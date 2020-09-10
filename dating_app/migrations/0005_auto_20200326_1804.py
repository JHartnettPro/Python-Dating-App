# Generated by Django 2.2 on 2020-03-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0004_auto_20200326_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='likes',
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='matches', to='dating_app.User'),
        ),
    ]