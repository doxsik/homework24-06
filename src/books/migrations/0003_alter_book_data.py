# Generated by Django 5.0.7 on 2024-07-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_remove_book_description_book_active_book_athor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book", name="data", field=models.IntegerField(null=True),
        ),
    ]