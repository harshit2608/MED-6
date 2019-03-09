from django.db import models

# Create your models here.
class Movie(models.Model):
    actor=models.CharField(max_length=30)
    movie_name = models.CharField(max_length=50)
    logo = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.actor

class song(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='movies')
    file_type=models.CharField(max_length=40)
    song_name=models.CharField(max_length=100)

