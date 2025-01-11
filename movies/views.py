from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))


def movie_detail(request, movie_id):
    movies = Movie.objects.get(pk = movie_id)
    template = loader.get_template('detail.html')
    context = {
        'movies': movies
    }
    return HttpResponse(template.render(context, request))