# Generated by Django 4.0.6 on 2022-08-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facts', '0003_alter_category_options_alter_fact_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
