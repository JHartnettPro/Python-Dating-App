# Generated by Django 2.2 on 2020-03-25 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('admin', models.BooleanField()),
                ('email', models.CharField(max_length=254)),
                ('age', models.IntegerField()),
                ('nickname', models.CharField(max_length=60)),
                ('photo', models.ImageField(upload_to='profile_images')),
                ('gender', models.BooleanField()),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like', models.ManyToManyField(related_name='likes', to='dating_app.User')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='dating_app.Message')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page', to='dating_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='dating_app.User'),
        ),
    ]
