from django.views import generic

from .models import Director, Movies

class IndexView(generic.ListView):
    template_name = 'movies/directors.html'
    model = Director

class DirectorView(generic.DetailView):
    template_name = 'movies/director.html'
    model = Director

class MovieView(generic.DetailView):
    template_name = 'movies/movie.html'
    model = Movies
