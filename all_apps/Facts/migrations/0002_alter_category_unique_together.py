# Generated by Django 4.0.6 on 2022-08-09 08:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Facts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('category', 'user_added')},
        ),
    ]
