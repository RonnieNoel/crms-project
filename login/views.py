from django.shortcuts import render, redirect
from login.validation_form import RegisterUserForm
from login.models import Crime, User,Suspect
from login.login_form_validation import LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import hashers, login, authenticate
from dashboard.views import DashView,UserDashView

def LogoutView(request):
    logout(request)
    return redirect(HomeView)

def HomeView(request):
    crime_count = Crime.objects.count()
    user_count = User.objects.count()
    suspect_count = Suspect.objects.count()
    return render(request, 'Homepage.html', {'crime_count': crime_count, 'user_count': user_count, 'suspect_count': suspect_count})

def LoginView(request):
    return render(request,'login.html') 


def RegisterView(request):
    if request.method =='POST':
        form= RegisterUserForm(request.POST)

        if form.is_valid():
            email_data=form.cleaned_data['email']
            password_data=form.cleaned_data['password']

            hashed_password=hashers.make_password(password_data)
            new_user=User(email=email_data,password=hashed_password)
            new_user.save()
            print("Registration successful")
            return render(request,'register.html')
        
        else:
            print("Registration failed")
            return render(request,"register.html")
    return render(request,'register.html')



def AuthenticationView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            emailT = form.cleaned_data['email']
            passwordT = form.cleaned_data['password']

            result = authenticate(request, username = emailT, password = passwordT)
            print(result)
            
            if result:
                login(request, result)
                print("success")
                return redirect(UserDashView)
            else:
                messages.error(request, "Invalid login credentials")
                print("fail")
        else:
            print("something went wrong")
            print(form.errors)

    return render(request, "login.html")

