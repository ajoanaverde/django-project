from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    # check si quelqu'un est loggé
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #autentification
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Vou avez été Loggé")
            return redirect('home')
        else:
            messages.success(request, "Il y a eu un error dans le login, reessayez postieurement")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Vous avez logout")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})