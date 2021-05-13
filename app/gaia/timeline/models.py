from django.db import models

from base.models import BaseModel
from project.models import Project


class Timeline(BaseModel):
    """
    A timeline is a starting point for any Project.
    One project can have many timelines, and all the smaller entities are part of the timeline.
    """

    era = models.CharField(max_length=200, help_text="E.g. Jurrassic, Stone Age, Satayuga etc.")
    start_period = models.BigIntegerField(help_text="E.g. 1914, 2000, 420 etc.")
    end_period = models.BigIntegerField(help_text="E.g. 1914, 2000, 420 etc.")
    label = models.CharField(max_length=4, help_text="E.g. BC, AD, BCE etc.")

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="timelines")

    def __str__(self):
        return f"{self.era} : {self.start_period} - {self.end_period} {self.label}"


class Event(BaseModel):
    """
    A notable event that has taken place in a timeline.
    An event can be associated with any character or place.
    """

    heading = models.CharField(max_length=500, help_text="E.g. First World War, Battle of Bastards etc.")
    description = models.TextField(help_text="Details of the event.")

    time_started = models.CharField(max_length=20, help_text="E.g. 1914, 320 BC etc.")
    time_ended = models.CharField(max_length=20, help_text="E.g. 1918, Present etc.")

    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE, related_name="events")

    def __str__(self):
        return f"{self.heading} : Started in {self.time_started} - Ended in {self.time_ended}"