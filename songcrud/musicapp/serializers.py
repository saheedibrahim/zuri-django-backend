from dataclasses import fields
from rest_framework import serializers
from .models import Artiste, Song, Lyric
# from . import models

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = "__all__"

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = "__all__"