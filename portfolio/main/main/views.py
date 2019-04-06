from django.shortcuts import render 
from django.http import HttpResponse

#Create views here

# each 'function' is a view
def homepage(request):
    return HttpResponse("<strong>Shea Winkler</strong>")