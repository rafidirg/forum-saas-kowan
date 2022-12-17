from authapp.forms import AppUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect


def register_view(request):
    form = AppUserCreationForm()

    if request.method == 'POST':
        form = AppUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authapp:login')

    context = {'form': form}
    return render(request, 'authapp/register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('forum:home')
        else:
            messages.info(request, 'Username or password not match')
    return render(request, 'authapp/login.html', {})


def logout_view(request):
    logout(request)
    return redirect('landing:home')
