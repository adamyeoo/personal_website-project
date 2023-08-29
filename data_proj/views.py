## views.py
## This is where the URL paths from urls.py specificies what they want to send
## Essentially, it's a list of functions that take in URL requests and returns HTTP responses

from django.shortcuts import render
from .models import DataProj # imports the Home class from model.py

# Create your views here.
def homepage(request):
    data_projects = DataProj.objects # now we can use all the Home objects
    return render(request, 'homepage.html', {'data_projects': data_projects}) # <- we pass in the jobs objects as a parameter to be used in homepage.html