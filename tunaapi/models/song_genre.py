from django.db import models

class SongGenre(models.Model):
    song = models.ForeignKey('tunaapi.Song', on_delete=models.CASCADE, related_name='song_genres')
    genre = models.ForeignKey('tunaapi.Genre', on_delete=models.CASCADE, related_name='song_genres')

    class Meta:
        unique_together = ('song', 'genre')