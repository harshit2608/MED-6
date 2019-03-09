from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'movie1/index.html',{})

def detail(request,movie_id):
    return HttpResponse("<h1> Welcome in id: "+str(movie_id)+"</h1>")