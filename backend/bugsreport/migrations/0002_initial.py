# Generated by Django 4.0 on 2023-09-01 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('bugsreport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugsreport',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
