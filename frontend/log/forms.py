#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control','style':'height:30px', 'name': 'username','placeholder': 'username',}))
							   						   
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control','style':'height:30px', 'name': 'password', 'placeholder': 'password',}))