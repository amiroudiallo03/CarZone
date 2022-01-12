from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from account.models import MyUser
from carzoneapp import models
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):

    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST["confirm_password"]

        if password != password2:
            messages.error(request, 'les mots de passe doivent etre identique')
            return redirect ('signup')
        forms = SignupForm({"firstname":firstname, "lastname":lastname, "username":username, "email":email, "password":password})
        user = MyUser.objects.create_user(email=email, first_name=firstname, last_name=lastname, username=username, password=password)
        print(request.user.id)
        return redirect ('index')
    return render(request, 'signup.html', locals())

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'email ou mot de passe incorrect')
            return redirect('login')

    return render(request, 'login.html', locals())