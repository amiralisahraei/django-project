# Generated by Django 4.2.9 on 2024-01-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_rename_marriage_user_married'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('married', models.BooleanField(db_column='marriage', null=True)),
                ('joined_date', models.DateField(null=True)),
                ('user_image', models.ImageField(null=True, upload_to='images/')),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
