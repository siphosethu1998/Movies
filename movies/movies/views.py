from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def home(request):
    return HttpResponse('<h1>Home of Movies</h1>') 

def add(request):
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
    return redirect('add')

def update(request, id):
    movie = Movie.objects.get(pk=id)
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie.title = title
        movie.year = year
        movie.save()
        return redirect('add')
    return render(request, 'movies/update.html', {'movie': movie}) 
 
