# Generated by Django 4.2.9 on 2024-01-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_user_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
