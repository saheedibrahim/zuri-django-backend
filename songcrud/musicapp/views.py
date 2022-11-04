from django.shortcuts import render
from rest_framework import generics
from .serializers import SongSerializer, ArtisteSerializer, LyricSerializer
from .models import Artiste, Song, Lyric

# Create your views here.
class CreateSongViews(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class GetSongViews(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class GetArtisteViews(generics.ListAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class UpdateSongViews(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class DeleteSongViews(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer