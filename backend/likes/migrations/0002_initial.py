# Generated by Django 4.0.6 on 2023-08-17 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlikes',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_likes', to='posts.post'),
        ),
    ]
