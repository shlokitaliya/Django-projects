from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.urls import reverse
from .forms import RegistrationForm, LoginForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list:index')  # Redirect to homepage or login page
    else:
        form = RegistrationForm()
    return render(request, 'user_registration.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)  # Pass `request` to form for AuthenticationForm
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('list:task_list')  # Redirect to task list or dashboard
        else:
            form.add_error(None, "Invalid username or password")  # Optional: better UX
    else:
        form = LoginForm()

    return render(request, 'user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('list:index')
