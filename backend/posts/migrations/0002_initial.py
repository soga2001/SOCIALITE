# Generated by Django 4.0 on 2023-09-01 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posted', to='users.user'),
        ),
        migrations.AddConstraint(
            model_name='post',
            constraint=models.CheckConstraint(check=models.Q(('img_url__isnull', False), ('caption__isnull', False), _connector='OR'), name='posts_post_either_img_url_or_caption'),
        ),
    ]
