from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tunaapi.views import ArtistViewSet, GenreViewSet, SongViewSet, SongGenreViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'artists', ArtistViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'songs', SongViewSet)
router.register(r'songgenres', SongGenreViewSet)

for url in router.urls:
    print(url)

urlpatterns = [
    path('', include(router.urls)),
]
