from http.cookiejar import request_path

from django.contrib.admin.templatetags.admin_list import search_form
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
import random
from django.template.defaultfilters import title
from django.db.models import Q
from unicodedata import category

from posts.models import Post
from posts.forms import PostCreateForm, SearchForm
from django.contrib.auth.decorators import login_required


def main_view(request):

    return render(request, 'main.html')

@login_required(login_url="/login")
def posts_list_view(request):
    search_form = SearchForm()
    if request.method == 'GET':
        search = request.GET.get("search")
        category = (
            int(request.GET.get("category")) if request.GET.get("category") else None
        )
        ordering = request.GET.get("ordering")
        page = int(request.GET.get("page", 1))
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) |
                                 Q(description__icontains=search)
                                 )
        if category:
            posts = posts.filter(category_id=category)
        if ordering:
            posts = posts.order_by(ordering)
        limit = 4
        max_pages = posts.count()/ limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = page * limit

        posts = posts[start:end]

        context_data = {"posts":posts, "search_form": search_form, "max_pages": range(1, max_pages+1)}

    return render(request, "posts/post__list.html",
                  context=context_data)

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
















