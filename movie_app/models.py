from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Movie(models.Model):

    CURRENCY_CHOICES = [
        ('E', 'Euro'),
        ('D', 'Dollar'),
        ('R', 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000)
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES, default='R')
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'

# from movie_app.models import Movie

