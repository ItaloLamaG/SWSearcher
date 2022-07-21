from django.db import models
from sw.models.film import Film


class Historic(models.Model):
    film = models.ForeignKey(Film, related_name="historic", on_delete=models.PROTECT)
    search_date = models.DateTimeField(auto_now_add=True)
