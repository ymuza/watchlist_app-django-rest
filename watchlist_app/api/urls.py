from django.urls import path
from watchlist_app.api.views import movie_details, movie_list
urlpatterns = [
    path('list/', movie_list, name='movie_list'),
    path('<int:pk>', movie_details, name='movie_detail'),
]