## views.py
## This is where the URL paths from urls.py specificies what they want to send
## Essentially, it's a list of functions that take in URL requests and returns HTTP responses
from django.http import HttpResponse ## to return HTTP response as a string...
from django.shortcuts import render ## to return HTTP response as HTML file

def home(request):
    return render (request, 'home.html')

def blog(request):
    return render (request, 'blog.html')