from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from forum.models import Post, Comment
from forum.forms import PostForm, CommentForm
from authapp.models import AppUser


def get_appuser_object(user):
    return AppUser.objects.get(username=user.username)


@login_required
def home(request):
    user = get_appuser_object(request.user)
    posts = Post.objects.filter(course_id=user.course_id).order_by('date')
    context = {
        'posts': posts
    }
    return render(request, 'forum/home.html', context)


@login_required
def create(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = get_appuser_object(request.user)
        form = form.save(commit=False)
        form.author = user
        form.course = user.course
        form.save()
        return redirect('/forum/')
    context = {
        'form': form,
    }
    return render(request, 'forum/create.html', context)


@login_required
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)
    form = CommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = get_appuser_object(request.user)
        form = form.save(commit=False)
        form.author = user
        form.post = post
        form.course = user.course
        form.save()
        return redirect(f'/forum/{post.slug}')

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'forum/detail.html', context)


