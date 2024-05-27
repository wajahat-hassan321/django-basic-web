from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('book_content/<int:pk>/', views.book_content, name='book'),
    path('add_book/', views.addbook, name='addbook'),
    path('update_book/<int:pk>/', views.book_update, name='update'),
    path('', views.register, name='register'),
    path('login/', views.user_Login, name='login'),
    path('likes/<int:pk>/',views.book_likes,name='likes'),
    path('liked_books/',views.liked_books,name='liked_books'),
    path('fav_books/<int:pk>/',views.favourites_book,name='fav_books'),
    path('book_search/',views.book_search,name='book_search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
