from django.db import models
from django.urls import reverse

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

    domain = models.ForeignKey('self', on_delete=models.CASCADE, related_name='places_within', null=True, blank=True)
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE, related_name='places')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("place:place-detail", kwargs={"pk": self.pk})


class Event(BaseModel):
    """
    A notable event that has taken place in a timeline.
    An event can be associated with any character or place.
    """

    heading = models.CharField(max_length=500, help_text="E.g. First World War, Battle of Bastards etc.")
    description = models.TextField(help_text="Details of the event.")

    time_started = models.CharField(max_length=20, help_text="E.g. 1914, 320 BC etc.")
    time_ended = models.CharField(max_length=20, help_text="E.g. 1918, Present etc.")

    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="events")

    def __str__(self):
        return f"{self.heading} : Started in {self.time_started} - Ended in {self.time_ended}"

    def get_absolute_url(self):
        return reverse("place:event-detail", kwargs={"pk": self.pk})
