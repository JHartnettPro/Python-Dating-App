# Generated by Django 2.2 on 2020-03-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0003_auto_20200326_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='likes',
            field=models.ManyToManyField(related_name='matches', to='dating_app.User'),
        ),
        migrations.DeleteModel(
            name='Profile_page',
        ),
    ]