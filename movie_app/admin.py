from django.contrib import admin
from .models import Movie

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status']
    list_editable = ['rating', 'year', 'budget']
    ordering = ['-rating', '-name']
    list_per_page = 10

    @admin.display(ordering='rating', description='status')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'This movie with bad reviews'
        if mov.rating < 70:
            return 'You can watch this movie one time'
        if mov.rating <= 85:
            return 'It\'s worth to be watch'
        return 'It\'s excellent movie'



