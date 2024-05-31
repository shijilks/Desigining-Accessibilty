from django.contrib.auth import views as auth_view
from django.urls import path 
from . import views
from.forms import LoginForm
urlpatterns = [
     path('', views.home),
     path('about/', views.about,name="about"),
     path('contact/', views.contact,name="contact"),
     path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
     path('profile/', views.ProfileView.as_view(),name="profile"),

     
    path('registration/', views.CustomerRegistrationView.as_view(),name="customerregistration"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm) ,name="login"),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

]