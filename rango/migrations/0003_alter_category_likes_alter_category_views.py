# Generated by Django 4.1.6 on 2023-02-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rango", "0002_alter_category_options_category_likes_category_views_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="category",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]