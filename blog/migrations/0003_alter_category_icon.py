# Generated by Django 5.1.4 on 2025-01-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_category_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to='category_icons/'),
        ),
    ]
