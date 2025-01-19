from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
import random
from posts.models import Post

def main_view(request):
    return render(request, 'main.html')


def posts_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
    return render(request, "post__list.html", context={"posts": posts})

def posts_detail_view(request, id):
     if request.method == 'GET':
         posts = Post.objects.get(id=id)
     return render(request, "post_detail.html", context={"post": posts})

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post_data = {
#         "id": post.id,
#         "title": post.title,
#         "description": post.description,
#         "created_at": post.created_at,
#         "updated_at": post.updated_at,
#     }
#     return JsonResponse(post_data)




