from django.db import models

from movie.models import Movie


class Rating(models.Model):
    product = models.ForeignKey(Movie, related_name='rating',
                                on_delete=models.CASCADE)
    one = models.PositiveIntegerField(default=0, null=True, blank=True)
    two = models.PositiveIntegerField(default=0, null=True, blank=True)
    three = models.PositiveIntegerField(default=0, null=True, blank=True)
    four = models.PositiveIntegerField(default=0, null=True, blank=True)
    five = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = []

    def __str__(self):
        # Extract all rating values and return max key.
        # Reverse this Dict if there is a tie and you want the last key.
        rating_list = {
            '1': self.one,
            '2': self.two,
            '3': self.three,
            '4': self.four,
            '5': self.five
        }
        return str(max(rating_list, key=rating_list.get))
