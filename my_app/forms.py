from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

#models form for books / register

from.models import books
class AddBook(ModelForm):
     class Meta:
         model=books
         fields = '__all__' 
         exclude=('likes',) 
 
 
class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
