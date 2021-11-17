from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
# Create your views here.


class Movies:
    @staticmethod
    def movie_list(self, request):
        self.movies = Movie.objects.all()
        self.data = {'movies': list(self.movies.values())}

        return JsonResponse(self.data)


