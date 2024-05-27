# Generated by Django 5.0 on 2024-04-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "my_app",
            "0003_bookgenre_books_book_content_remove_books_book_genre_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="books",
            name="second_author",
            field=models.ManyToManyField(
                blank=True,
                related_name="second_books_authored",
                to="my_app.authors_name",
            ),
        ),
    ]
