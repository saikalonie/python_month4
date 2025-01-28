from http.cookiejar import request_path

from django.contrib.admin.templatetags.admin_list import search_form
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
import random
from django.template.defaultfilters import title
from django.db.models import Q
from unicodedata import category

from posts.models import Post
from posts.forms import PostCreateForm, SearchForm, PostUpdateForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView

def main_view(request):
    if request == "GET":
        return render(request, 'main.html')

class TestView(View):
    def get(self, request):
        return HttpResponse("Test")



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

class PostListView(ListView):
    model = Post
    template_name = "posts/post__list.html"
    context_object_name = "posts"



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
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})

        elif form.is_valid:
            user =request.user
            Post.objects.create(**form.cleaned_data, author=user)
            return redirect("/profile/")

@login_required(login_url="/login")
def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id)  # Fetch the post by ID
    if request.method == "GET":
        form = PostUpdateForm(instance=post)  # Prepopulate form with the existing post
        return render(request, "posts/post_update.html", context={"form": form})
    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post)  # Bind form with POST data
        if form.is_valid():
            form.save()  # Save the updated post
            return redirect(f"/posts/{post_id}")  # Redirect to the post list view
        else:
            return render(request, "posts/post_update.html", context={"form": form})











