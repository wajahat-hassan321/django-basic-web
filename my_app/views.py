from django.shortcuts import render,redirect , get_object_or_404
from .models import books
from .forms import AddBook , Register
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def home(request):
    user=request.user
    username=request.user.username
    book=books.objects.all()
    context={'books':book,
             'user':username,
             'User':user}
    return render(request,'home.html',context=context)
@login_required(login_url='login')
def book_content(request,pk):
    book=books.objects.get(id=pk)
    return render(request,'detail_page.html',{'book':book})
@login_required(login_url='login')
def addbook(request):
    if request.method == 'POST':
      form=AddBook(request.POST,request.FILES)
      if form.is_valid():
          form.save()
          return redirect('home')
    else:
        form=AddBook()
     
    return render(request,'addbook.html',{'form':form})
@login_required(login_url='login')
def book_update(request,pk):
    book=books.objects.get(id=pk)
    form=AddBook(request.POST or None,instance=book)
    context={'form':form}
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'update.html',context=context)

def register(request):
 if request.method == 'POST':
    form = Register(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
 else:
    form = Register()
    
 return render(request, 'register.html', {'form': form})

def user_Login(request):
    if request.method=='POST':
     Username=request.POST.get('Username')
     Password=request.POST.get('Password')
     
     user=authenticate(request,username=Username,password=Password)
     if user is not None:
         login(request,user)
         return redirect('home')
     else:
         return redirect('register')    
    return render(request, 'login.html')

@login_required(login_url='login')
def book_likes(request,pk):
    book=get_object_or_404(books,id=pk)
    if book.likes.filter(id=request.user.id):
        book.likes.remove(request.user)
    else:
        book.likes.add(request.user)
    return redirect('home')
@login_required(login_url='login')
def liked_books(request):
    user=request.user
    liked_book=books.objects.filter(favourites=user)
    return render(request,'liked.html',{'books':liked_book})


def favourites_book(request,pk):
    book=get_object_or_404(books,id=pk)
    if book.favourites.filter(id=request.user.id):
        book.favourites.remove(request.user)
    else:
        book.favourites.add(request.user)
    return redirect('home')



def userlogout(request):
    logout(request.user)
    return redirect('register')

def book_search(request):
    query = request.GET.get('search')

    
    book_query = Q(book_name__icontains=query)
    author_query = Q(book_author__name__icontains=query)   
    genre_query = Q(book_genre__genre__icontains=query)  

     
    combined_query = book_query | author_query | genre_query
    book_results = books.objects.filter(combined_query)

    context = {'books': book_results, 'query': query}
    return render(request, 'searched.html', context)