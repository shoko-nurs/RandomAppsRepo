# Generated by Django 3.2.9 on 2022-08-02 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Facts', '0002_alter_fact_from_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user_added',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='User.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fact',
            name='user_added',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='User.customuser'),
            preserve_default=False,
        ),
    ]
