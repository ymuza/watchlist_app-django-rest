from rest_framework import serializers  # tengo que importar la clase serializers para indicar que los voy a usar.
from models import Movie

class MovieSerializer(serializers.Serializer):  # si la tabla en models es 'Movie', asi tambien el serializer.
    id = serializers.IntegerField(read_only=True)  # acá comienza la traducción de los datos. El id es read_only.
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


