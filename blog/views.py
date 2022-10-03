from typing import Text
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from .models import Game, Post, Category
from .forms import RegisterForm
from django.core.paginator import Paginator

def index(request):
    posts = Post.objects.filter(pub = 1).order_by('-date')[:16]
    most_pop = Post.objects.filter(pub = 1).filter(view__gte = 1).order_by('-view')[:4]
    categories = Category.objects.all()[:10]
    context = {'posts':posts, 'categories': categories , 'most_pop': most_pop}
    return render(request, 'blog/index.html', context)

def category(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug__exact=slug)
    post=Post.objects.filter(category=category).order_by('-date')
    most_popular = Post.objects.filter(pub = 1).order_by('-date')[:16]
    return render(request,'blog/category.html', {'categories':categories,'category':category,'post':post,'most_popular':most_popular})

def posts(request):
    posts = Post.objects.filter(pub = 1).order_by('-date')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    most_popular = Post.objects.filter(pub = 1).order_by('-date')
    context = {'page_obj': page_obj, 'most_popular':most_popular}
    return render(request, 'blog/posts.html', context)

def search_function(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(Q(title__icontains=query))
    search_obj = Game.objects.filter(Q(title__icontains=query))
    most_popular = Post.objects.filter(pub = 1).order_by('-date')[:10]
    context = {'query': query, 'search_obj':search_obj, 'most_popular':most_popular,}
    return render(request, 'blog/search.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug__exact = slug)
    category=Category.objects.all()
    most_popular = Post.objects.filter(pub = 1).order_by('-date')
    post.view += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post':post,'category':category,'most_popular':most_popular})

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = RegisterForm()
        return render(request, 'blog/register.html', {'form':form})
    return redirect('index')

def comment(request, slug):
    post = Post.objects.get(slug__exact=slug)
    if request.method == 'POST':
        post.comment_set.create(author = request.user, text = request.POST.get('text'))
        return redirect(reverse('post_detail_url', kwargs = {'slug': post.slug}))
    return redirect(reverse('post_detail_url', kwargs = {'slug': post.slug}))

def game_post(request):
    game = Game.objects.filter(pub=1).order_by('-date')
    most_popular = Post.objects.filter(pub = 1).order_by('-date')
    context = {'game':game,'most_popular': most_popular}
    return render(request, 'blog/game_post.html', context)

def game(request, slug):
    game = Game.objects.filter(slug__exact = slug)
    return render(request, 'blog/game.html', {'game':game})


