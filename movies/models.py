from django.db import models
from django.utils import timezone

class Genre(models.Model): # Genre inherits from models.Model
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)        #CASCADE = if a genre is deleted all movies within genre are deleted
    date_created = models.DateTimeField(default = timezone.now)