from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def home(request):
    return render(request, 'movies/base.html')

def add_show(request): # can add and show movies
    form = MovieForm()
    
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()

    movies = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': movies, 'form':form})

def detail(request, id):
    movie = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': movie})

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404("Movie does not exist")
    movie.delete()
    return redirect('add_show')

def update(request, id):
    movie = Movie.objects.get(pk=id)
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie.title = title
        movie.year = year
        movie.save()
        return redirect('add_show')
    return render(request, 'movies/update.html', {'movie': movie}) 
 
