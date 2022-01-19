from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<str:slug>/', views.DetailView.as_view(), name='detail_view'),
    path('signup', views.signup, name='signup'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('cars', views.cars, name='cars'),
    path('dashboard', login_required(views.DashboardView.as_view()), name='dashboard'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('service', views.ServiceView.as_view(), name='service'),
    path('search', views.search, name='search'),
]


