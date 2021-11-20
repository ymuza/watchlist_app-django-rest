from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie


# esta es una function based views (fbv)
@api_view()  # en las fbv, se agrega este decorador para poder saber que tipo de endpoint es. Si es vacio=GET.
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)  # many=true implica que el serializer tiene que buscar varios objects
    return Response(serializer.data)  # retorno los datos ya transformados.


@api_view()
def movie_details(request, pk):  # va a aceptar un request, y la pk.
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)  # como acá el queryset es uno, no tengo que agregar 'many=True'.
    return Response(serializer.data)  # retorno los datos ya transformados.



