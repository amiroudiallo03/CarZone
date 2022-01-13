from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from account.models import MyUser
from carzoneapp import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

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
        if password == password2:
            if MyUser.objects.filter(username=username).exists():
                messages.error(request, 'Username is already exists!')
                return redirect('signup')
            else:
                if MyUser.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already exists!')
                    return redirect('signup')
                else:
                    forms = SignupForm({"firstname":firstname, "lastname":lastname, "username":username, "email":email, "password":password})
                    if forms.is_valid():
                        user = MyUser.objects.create_user(email=email, first_name=firstname, last_name=lastname, username=username, password=password)
                        login(request, user)
                        messages.success(request, "You're now logged")
                        return redirect('dashboard')
        
            return redirect ('index')
    
    return render(request, 'signup.html', locals())

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'email ou mot de passe incorrect')
            return redirect('login')

    return render(request, 'login.html', locals())

def logout_view(request):
    
    logout(request)

    return redirect('login_view')
def cars(request):

    return render(request, "cars.html")


class DashboardView(TemplateView):
    template_name = "dashboard.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"

class ServiceView(TemplateView):
    template_name = "services.html"