from django.db import models
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse("timeline:timeline-detail", kwargs={"pk": self.pk})
