from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from core.models import Movie

class MovieDetail(DetailView):
    model = Movie

class MovieList(ListView):
    model = Movie
    paginator = Paginator(Movie,3)