from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post

def home(request):
    all_posts = Post.objects.all()
    dat = {'posts': all_posts}
    return render(request, "blog/home.html", context=dat)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # the convention: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, "blog/about.html")


