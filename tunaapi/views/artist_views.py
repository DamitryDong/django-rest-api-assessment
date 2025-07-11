from rest_framework import viewsets
from ..models.artist import Artist
from ..serializers import ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer