from django.db import models
import os
from django import forms

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='Imię')
    surname = models.CharField(max_length=50, verbose_name='Nazwisko')

    def __str__(self):
        return self.name + ' ' + self.surname

class Period(models.Model):
    name = models.CharField(max_length=100, verbose_name='Epoka literacka')
    description = models.CharField(max_length=1000, verbose_name='Opis')
    beginning = models.IntegerField(verbose_name='Rok rozpoczęcia')
    end = models.IntegerField(verbose_name='Rok zakończenia')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Tytuł')
    image = models.ImageField(verbose_name='Wykres', upload_to='bookapp/static/bookapp/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor')
    period = models.ForeignKey(Period, on_delete=models.CASCADE, verbose_name='Epoka literacka')
    def __str__(self):
        return self.title
    
    def get_name(self):
        return self.image.name[15:] 

class Text(models.Model):
    title = models.CharField(max_length=100, verbose_name="Tytuł")
    file = models.FileField(verbose_name="Plik", upload_to='uploads/')

    def __str__(self):
        return self.title

