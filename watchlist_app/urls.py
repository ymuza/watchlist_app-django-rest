from django.urls import path
from watchlist_app.views import Movies

urlpatterns = [
    path('list/', Movies.movie_list, name='movie_list'),
]
