from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
import datetime
from neulyferreira.core.models import Category
from neulyferreira.core.models import Post
from neulyferreira.core.models import Ad
from neulyferreira.core.models import About
from neulyferreira.core.models import Banner
# Create your views here.

def index(request):
    posts = Post.objects.all().filter(published=True).order_by('-created_at')[:3]
    categories = Category.objects.all()
    now = datetime.datetime.now()
    ads = Ad.objects.all()
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[0:1]
    banner = Banner.objects.all()[:1].get()
    senzala = Ad.objects.all()[:1].get()
    about = About.objects.all()[:1].get()
    template_name = 'posts/index.html'
    context = {
        'posts': posts,
        'categories': categories,
        'year': now.year,
        'ads': ads,
        'senzala': senzala,
        'recent_posts': recent_posts,
        'about': about,
        'banner': banner
    }
    return render(request, template_name, context)


def about(request):
    about = About.objects.get(id=1)
    template_name = 'about/about.html'
    context = {
        'about': about,

    }
    return render(request, template_name, context)


def contact(request):
    about = About.objects.get(id=1)
    template_name = 'contact/contact.html'
    context = {
        'contact': contact

    }
    return render(request, template_name, context)

def posts(request):
    posts_list = Post.objects.all().filter(published=True)
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    categories = Category.objects.all()
    now = datetime.datetime.now()
    ads = Ad.objects.all()
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[0:3]
    senzala = Ad.objects.get(id=1)
    about = About.objects.get(id=1)
    template_name = 'posts/posts.html'
    context = {
        'posts': posts,
        'categories': categories,
        'year': now.year,
        'ads': ads,
        'senzala': senzala,
        'recent_posts': recent_posts,
        'about': about
    }
    return render(request, template_name, context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.all()
    now = datetime.datetime.now()
    ads = Ad.objects.all()
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[0:3]
    senzala = Ad.objects.get(id=1)
    about = About.objects.get(id=1)
    template_name = 'posts/post_detail.html'
    context = {
        'post': post,

        'categories': categories,
        'year': now.year,
        'ads': ads,
        'senzala': senzala,
        'recent_posts': recent_posts,
        'about': about
    }
    return render(request, template_name, context)
