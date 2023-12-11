from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# Create your views here.
@login_required

# def login(request):
#     return render(request, 'registration/login.html')

def landing(request):
    return render(request, 'landingpage.html')

def camisas(request):
    return render(request, 'camisas.html')

# def salir(request):
#     logout(request)
#     return redirect(request, '/base.html')
