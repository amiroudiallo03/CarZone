from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from account.models import MyUser
from carzoneapp import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from django.db.models import Q


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banners"] = models.Banner.objects.all()
        context["cars"] = models.Car.objects.all()
        #context["brand"] = models.Brand.objects.all()
        context['city_search'] = models.Car.objects.values_list('location', flat=True).distinct()
        context['brand_search'] = models.Car.objects.values_list('brand', flat=True).distinct()
        context['year_search'] = models.Car.objects.values_list('year', flat=True).distinct()
        context['model_search'] = models.Car.objects.values_list('model', flat=True).distinct()
        return context

   
    
    # def get(self, request, *args, **kwargs):
    #     banners = models.Banner.objects.all()
    #     cars = models.Car.objects.filter(status=True).all()
    #     context = {
    #         'banners': banners,
    #         'cars': cars,
    #     }
    #     return render(request, self.template_name, context) 


class DetailView(DetailView):
    model = models.Car
    template_name = "detail/car-details.html"
    context_object_name = "car"

    # def get_object(self):
    #     obj = super().get_object()
    #     obj.save()

    #     return obj 



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
                    forms = SignupForm(request.POST)
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
            return redirect('login_view')

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

def search(request):
    search  = False
    cars = models.Car.objects.order_by('-date_add')
    city_search = models.Car.objects.values_list('location', flat=True).distinct()
    brand_search = models.Car.objects.values_list('brand', flat=True).distinct()
    year_search = models.Car.objects.values_list('year', flat=True).distinct()
    model_search = models.Car.objects.values_list('model', flat=True).distinct()
    transmission_search = models.Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            cars = models.Car.objects.filter(name__icontains=keyword)
    
    if 'brand' in request.GET:
        brand = request.GET["brand"]
        if brand:
            cars = models.Car.objects.filter(name__icontains=brand)

    if 'location' in request.GET:
        location = request.GET["location"]
        if location:
            cars = models.Car.objects.filter(location__icontains=location)
    
    if 'year' in request.GET:
        year = request.GET["year"]
        if year:
            cars = models.Car.objects.filter(year__icontains=year)
    
    if 'type' in request.GET:
        car_type = request.GET["type"]
        if car_type:
            cars = models.Car.objects.filter(description__icontains=car_type)
    
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)
    print(request.GET)
    
    return render(request, 'search.html', locals())


        
        


