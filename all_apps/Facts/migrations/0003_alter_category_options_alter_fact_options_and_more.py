# Generated by Django 4.0.6 on 2022-08-10 06:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Facts', '0002_alter_category_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterModelOptions(
            name='fact',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='category',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='fact',
            unique_together={('from_category', 'fact')},
        ),
    ]
