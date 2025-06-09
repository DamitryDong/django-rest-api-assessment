from django.db import models
from .artist import Artist
from .genre import Genre

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    length = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    genres = models.ManyToManyField(Genre, through='SongGenre', related_name='genre_songs')
    
    def __str__(self):
        return self.title