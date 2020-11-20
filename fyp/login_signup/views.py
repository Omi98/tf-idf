from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import logout
from django.contrib.auth.models import User, auth

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    return render(request, 'register.html')


def search_page(request):
    if request.user.is_authenticated:
        return render(request, 'search.html')
    else:
        return redirect('/login')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        gmail = request.POST['gmail']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return redirect('/register_page/')

        elif User.objects.filter(email=gmail).exists():
            return redirect('/register_page/')

        else:
            user = User.objects.create_user(username=username,
                                            email=gmail,
                                            password=password)
            user.save()
            return redirect('/login_page/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        login_username = request.POST['username']
        login_password = request.POST['password']

        user = auth.authenticate(username=login_username,
                                 password=login_password)

        if user is not None:
            auth.login(request, user)
            print('\n user logged in \n')
            return redirect('/search_page/')
        else:
            print('\n invalid credentials \n')
            return redirect('/login_page/')
    else:
        return redirect('/login_page/')


def logout(request):
    auth.logout(request)
    print('\n user logged out \n')
    return redirect('/home/')
