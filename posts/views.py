from django.shortcuts import render, HttpResponse
import random

def main_view(request):
    return HttpResponse( f"Hello, world! {random.randint(1, 100)}")

def html_view(request):
    return render(request, 'main.html')
