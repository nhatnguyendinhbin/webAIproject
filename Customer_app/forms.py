from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# đây là forms login


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
class ResgisterForm(UserCreationForm):
    class meta :
        model = User
        fields = ['username', 'email', 'password1','password2']