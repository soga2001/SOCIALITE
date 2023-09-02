# Generated by Django 4.0 on 2023-09-01 21:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=255)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
