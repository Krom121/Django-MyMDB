from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from core.models import Movie , Person

class MovieDetail(DetailView):
    model = Movie
    queryset = (Movie.objects.all_with_related_persons())

class MovieList(ListView):
    model = Movie
    paginator = Paginator(Movie,3)


class PersonDetail(DetailView):
    model = Person
    queryset = Person.objects.all_with_prefetch_movies()