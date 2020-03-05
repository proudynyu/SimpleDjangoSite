from django.shortcuts import render
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

def homepage(request):
    return render(
        request,
        'simplesite/homepage.html',
        context={'tutorials': Tutorial.objects.all()}
    )

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        user = form.save()

    form = UserCreationForm
    return render(
        request,
        'simplesite/register.html',
        context={'form':form}
    )
