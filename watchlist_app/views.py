# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
# # Create your views here.
#
#
# class Movies:
#     @staticmethod
#     def movie_list(self, request):
#         self.movies = Movie.objects.all()
#         self.data = {'movies': list(self.movies.values())}
#
#         return JsonResponse(self.data)
#
#
#     def movie_details(request,pk): # tomo la pk, entonces en la url le paso el numero de pelicula
#         movie = Movie.objects.get(pk=pk)  # busco la peli por pk, por ej: localhost/movie/1
#         data = {
#             'name': movie.name,
#             'description': movie.description,
#             'active': movie.active
#             }
#
