from http.cookiejar import request_path

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
import random
from django.template.defaultfilters import title
from posts.models import Post
from posts.forms import PostCreateForm
from django.contrib.auth.decorators import login_required


def main_view(request):

    return render(request, 'main.html')

@login_required(login_url="/login")
def posts_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
    return render(request, "posts/post__list.html", context={"posts": posts})

@login_required(login_url="/login")
def posts_detail_view(request, post_id):
     if request.method == 'GET':
         posts = Post.objects.get(id=post_id)
     return render(request, "posts/post_detail.html", context={"post": posts})

@login_required(login_url="/login")
def post_create_view(request):
    if request.method == "GET":
        form = PostCreateForm()
        return render(request, "posts/post_create.html", context={"form": form})

    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # image = form.cleaned_data.get("image")
            # title = form.cleaned_data.get("title")
            # description = form.cleaned_data.get("description")
            # Post.objects.create(image=image, title=title, description=description)
            form.save()
            return redirect("/posts/")
        else:
            return render(request, "posts/post_create.html", context={"form": form})

