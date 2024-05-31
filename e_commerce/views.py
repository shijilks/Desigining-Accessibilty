from django.db.models import Count
from django.views import View
from .models import Product,Customer
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.urls import reverse
from .forms import CustomerProfileForm,CustomerRegistrationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registered Successfully")
            return redirect(reverse('login'))  # Redirect to login page
        else:
            messages.warning(request, "Invalid input data")
        return render(request, 'customerregistration.html', {'form': form})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the same page after submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,'category.html',locals())
    

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        
        if request.user.is_authenticated:
          
         return render(request,'profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg =Customer(user=user,name=name,locality=locality,city=city,mobile=mobile, state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! User Register Successfully")
        else:
            messages.warning(request,"Invaild input Data")
        return render(request,'profile.html',locals())


