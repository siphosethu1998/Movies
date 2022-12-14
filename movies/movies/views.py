from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import Movie

def home(request):
    return HttpResponse('<h1>Home</h1>') 

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/movies.html') 

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404("Movie does not exist")
    movie.delete()
    return HttpResponseRedirect('/movies')

def update(request, id):
    movie = Movie.objects.get(pk=id)
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie.title = title
        movie.year = year
        movie.save()
        return redirect('movies')
    return render(request, 'movies/update.html', {'movie': movie}) 
 
