from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def myview(request):
    print('request:', request)
    return render(request, "index.html", {})

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('/')
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
            
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            return redirect('/')
        else: 
            messages.error(request, 'Username or password is incorrect')
            
    return render(request, 'pizza_system/login_register.html' )

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        # creates instance of form
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # temporarily hold user data
            user = form.save(commit=False)
            user.username = user.username.lower()
            # adds user to database
            user.save()
            
            messages.success(request, f'Account created for {user}!')
                # registered user is now logged in
            login(request, user)
            return redirect('home')
        
        else: 
            
            messages.error(request, 'An error has occurred during registration')

    
    context = {'page': page, 'form': form}
    return render(request, 'pizza_system/login_register.html', context)

# todo list views

def index(response):
    return HttpResponse("<h1>tech with John</>")

def v1(response):
    return HttpResponse("<h1>view 1</h1>")

