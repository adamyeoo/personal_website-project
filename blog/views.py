from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, './allblogs.html', {'blogs': blogs})


def details(request, blog_id): # takes in a blog_id to return the corresponding info from that particular blog
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, './details.html', {'blog':detail_blog})