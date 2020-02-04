from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Group
from .forms import PostForm


def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group = group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group":group, "posts":posts})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.author = request.user
            Post.text = form.cleaned_data['text']
            Post.group = form.cleaned_data['group']
            form.save()
            return redirect('index')
        return render(request, 'new.html', {'form':form})
    form = PostForm()
    return render(request, 'new.html', {'form':form})
    