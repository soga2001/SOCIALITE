# Generated by Django 4.0.6 on 2023-07-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
