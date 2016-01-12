from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django import forms
from .forms import PostForm

def post_list(request):
    log = False
    username = ''
    if request.user.is_authenticated():
        log = True
        username = request.user
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'log' : log, 'username' : username})

def post_detail(request, pk):
    edit = False
    if request.user.is_staff:
        edit = True
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'edit_button': edit})

def post_new(request):
    if not request.user.is_authenticated ():
        return render(request, 'blog/no.html')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
