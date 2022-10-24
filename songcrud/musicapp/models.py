from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 400)
    last_name = models.CharField(max_length = 400)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.ForeignKey(Artiste, on_delete = models.PROTECT)
    date_released = models.DateField(default = datetime.today)
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length = 400)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.ForeignKey(Song, on_delete = models.PROTECT)
    song_id = models.CharField(max_length = 400)

    def __str__(self):
        return self.content


