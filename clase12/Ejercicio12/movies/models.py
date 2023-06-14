from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    born_date = models.DateField()
    dead_date = models.DateField(null= True, blank = True)
    biography = models.TextField()
    image = models.URLField()

    def __str__(self):
        return f'{self.name} {self.last_name}'
    
class Movies(models.Model):
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    movie_name = models.CharField(max_length=50)
    sinopsis = models.TextField()
    length_time = models.PositiveIntegerField()
    image = models.URLField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.movie_name
