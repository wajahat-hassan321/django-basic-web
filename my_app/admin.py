from django.contrib import admin
from .models  import books,Authors_Name,BookGenre

# Register your models here.
admin.site.register(books)
admin.site.register(Authors_Name)
admin.site.register(BookGenre)

