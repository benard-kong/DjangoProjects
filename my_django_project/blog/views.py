from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

test_data = [
            {"title": "Post1",
             "author": "ME"},
            {"title": "Post2",
             "author": "YOU"}
             ]

def home(request):
    all_posts = Post.objects.all()
    dat = {'posts': all_posts}
    return render(request, "blog/home.html", context=dat)
