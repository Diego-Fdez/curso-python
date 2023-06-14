from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text='Escribe el genero')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=64, help_text='Escribe el titulo')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(help_text='Escribe el año')
    genre = models.ManyToManyField(Genre)
    summary = models.TextField(max_length=100, help_text='Escribe una breve descripcion')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID Único para este libro')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200, help_text='Escribe el nombre de la editorial')
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    first_name = models.CharField(max_length=64, help_text='Escribe el nombre')
    last_name = models.CharField(max_length=64, help_text='Escribe el apellido')
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'