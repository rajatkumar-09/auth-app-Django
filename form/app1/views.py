from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def home(request):


    return render(request, 'Home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Password and Confirm Password are not same")
        else:
            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def login_view(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            auth_login(request, user)    
            return redirect("home")
        else:
            return HttpResponse("Username or Password is incorrect!!")

    return render(request, 'login.html')
def logout_view(request):
    auth_logout(request)  
    return redirect('login')
    

