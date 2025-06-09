from rest_framework import serializers
from .models.artist import Artist
from .models.genre import Genre
from .models.song import Song
from .models.song_genre import SongGenre


class ArtistSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()
    song_count = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ['id', 'name', 'age', 'bio', 'song_count', 'songs']

    def get_song_count(self, obj):
        return obj.songs.count()

    def get_songs(self, obj):
        songs = obj.songs.all()
        return [
            {
                'id': song.id,
                'title': song.title,
                'album': song.album,   
                'length': song.length  
            }
            for song in songs
        ]
        
class GenreSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ['id', 'description', 'songs']

    def get_songs(self, obj):
        songgenres = SongGenre.objects.filter(genre=obj)
        songs = [sg.song for sg in songgenres]
        return SongSerializer(songs, many=True).data

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist',
        write_only=True
    )
    artist_id_read = serializers.IntegerField(source='artist.id', read_only=True)
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Song
        fields = ['id', 'title', 'album', 'length', 'artist', 'artist_id', 'artist_id_read', 'genres']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Rename artist_id_read to artist_id for output
        rep['artist_id'] = rep.pop('artist_id_read')
        return rep


class GenreSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ['id', 'description', 'songs']

    def get_songs(self, obj):
        # assuming SongGenre has song and genre foreign keys
        songgenres = SongGenre.objects.filter(genre=obj)
        songs = [sg.song for sg in songgenres]
        return SongSerializer(songs, many=True).data


class SongGenreSerializer(serializers.ModelSerializer):
    song_id = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(),
        source='song'
    )
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        source='genre'
    )

    class Meta:
        model = SongGenre
        fields = ['id', 'song_id', 'genre_id']