# Generated by Django 4.2.9 on 2024-01-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_alter_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='marriage',
            field=models.BooleanField(db_column='marriage', null=True),
        ),
    ]
