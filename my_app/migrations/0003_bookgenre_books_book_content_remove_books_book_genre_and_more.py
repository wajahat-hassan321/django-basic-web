# Generated by Django 5.0 on 2024-04-10 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0002_authors_name_remove_books_book_author_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookGenre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("genre", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="books",
            name="book_content",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="books",
            name="book_genre",
        ),
        migrations.AddField(
            model_name="books",
            name="book_genre",
            field=models.ManyToManyField(to="my_app.bookgenre"),
        ),
    ]