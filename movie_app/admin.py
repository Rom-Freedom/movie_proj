from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['-rating', '-name']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name__startswith', 'rating']

    @admin.display(ordering='rating', description='status')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'This movie with bad reviews'
        if mov.rating < 70:
            return 'You can watch this movie one time'
        if mov.rating <= 85:
            return 'It\'s worth to be watch'
        return 'It\'s excellent movie'
    @admin.action(description='To set currency as dollar')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)
    @admin.action(description='To set currency as euro')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'{count_updated} entries have been updated',
            messages.ERROR
        )







