from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from user.forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "register/register.html", context={"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, "register/register.html", context={"form":form})
        elif form.is_valid():
            User.objects.create_user(
                username = form.cleaned_data["username"],
                email = form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            return redirect("main_view")

def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "register/login.html", context={"form": form})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, "register/login.html", context={"form": form})
        elif form.is_valid():
            user = authenticate(**form.cleaned_data)
            if not user:
                form.add_error(None, "Invalid username or password")
                return render(request, "register/login.html", context={"form": form})
            elif user:
                login(request, user)
                return redirect("main_view")

def logout_view(request):
    logout(request)
    return redirect("main_view")








