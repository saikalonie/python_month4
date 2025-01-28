from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from posts.models import Post
from user.forms import RegisterForm, LoginForm
from user.models import Profile
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "register/register.html", context={"form": form})
    if request.method == "POST":
        print(request.POST, request.FILES)

        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "register/register.html", context={"form":form})
        elif form.is_valid():
            form.cleaned_data.__delitem__("password_confirm")
            image = form.cleaned_data.pop("image")
            age = User.cleaned_data.pop("age")
            user = User.objects.create_user(
                **form.cleaned_data
            )
            Profile.objects.create(
                user=user,
                image=image,
                age=age,
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
@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect("main_view")

@login_required(login_url="/login/")
def profile_view(request):
    if request.method == "GET":
        user = request.user
        posts = Post.objects.filter(author=user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        return render(request, "register/profile.html", context={"profile": profile, "posts": posts})









