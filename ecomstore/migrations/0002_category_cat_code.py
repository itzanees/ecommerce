# Generated by Django 5.1 on 2024-10-19 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_code',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
