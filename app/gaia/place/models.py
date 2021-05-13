from django.db import models

from base.models import BaseModel
from timeline.models import Timeline


class Place(BaseModel):
    """
    A place is a location in space where characters can live and events can happen.
    One place can have many other places.
    A place is the most important entity in a project as plots can revolve around places.
    """

    name = models.CharField(max_length=200, help_text="E.g. Earth, Dimension 616, Delhi etc.")
    description = models.TextField(help_text="Some description of the place.")

    domain = models.ForeignKey('self', on_delete=models.CASCADE, related_name='places_within')
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE, related_name='places')

    def __str__(self):
        return self.name
