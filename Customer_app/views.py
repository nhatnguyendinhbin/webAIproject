from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate



# Create your views here.
def sign_in(request):
    if request.method =='GET':
        form = LoginForm()
        # return render(request,'user/login.html',{'form':form})
        return render(request,'login.html',{'form':form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('home')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        # return render(request,'user/login.html',{'form': form})
        return render(request,'login.html',{'form': form})
        
    
def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('home')

