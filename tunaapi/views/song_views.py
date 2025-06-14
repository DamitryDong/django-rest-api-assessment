from rest_framework import viewsets
from ..models.song import Song
from ..serializers import SongSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer