from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

def homepage(request):
    return render(
        request,
        'simplesite/homepage.html',
        context={'tutorials': Tutorial.objects.all()}
    )

def register(request):
    if request.method=='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User created: {username}')
            login(request, user)
            return redirect("/")
            
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')

            return render(
                request,
                'simplesite/register.html',
                context={'form':form}
            )

    form = NewUserForm
    return render(
        request,
        'simplesite/register.html',
        context={'form':form}
    )

def logout_request(request):
    logout(request)
    messages.info(request, f'Successfully logout')
    return redirect('/')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST )
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{username} is logged')
                return redirect('/')
            else:
                messages.error(request, f'Invalid username or password')
        else:
            messages.error(request, f'Invalid username or password')

    form = AuthenticationForm()
    return render(
        request,
        'simplesite/login.html',
        context={'form':form}
    )