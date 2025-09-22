from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'simpleblog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # Use get_object_or_404 instead of .get()
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'simpleblog/post_detail.html', {'post': post})