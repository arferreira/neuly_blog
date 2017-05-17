from django.shortcuts import render
from neulyferreira.core.models import Category
from neulyferreira.core.models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    template_name = 'posts/index.html'
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, template_name, context)
