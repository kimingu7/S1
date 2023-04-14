# Generated by Django 3.2.12 on 2023-04-14 05:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0003_remove_comment_parent_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='dislike_users',
            field=models.ManyToManyField(related_name='dislike_boards', to=settings.AUTH_USER_MODEL),
        ),
    ]
