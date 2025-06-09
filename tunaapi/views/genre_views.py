from rest_framework import viewsets
from ..models.genre import Genre
from ..serializers import GenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer