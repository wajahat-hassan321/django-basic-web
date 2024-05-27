from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Authors_Name(models.Model):
    name=models.CharField(max_length=50,blank=False)
    
    def __str__(self):
        return self.name


class BookGenre(models.Model):
    genre=models.CharField(max_length=100)
    
    def __str__(self):
        return self.genre

class books(models.Model):
    book_name=models.CharField(max_length=100)
    book_image=models.ImageField(blank=True)
    book_author=models.ManyToManyField(Authors_Name,default="authors")
    second_author=models.ManyToManyField(Authors_Name,blank=True, related_name='second_books_authored')
    book_content=models.TextField(null=False)
    book_genre=models.ManyToManyField(BookGenre)
    likes=models.ManyToManyField(User,related_name='blog_posts', blank=True)
    favourites=models.ManyToManyField(User,blank=True,default=False)
  
  
  
    def count_likes(self):
        return self.likes.count()
        
  
  
    def __str__(self) -> str:
        return self.book_name