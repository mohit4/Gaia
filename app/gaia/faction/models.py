from django.db import models

from base.models import BaseModel
from place.models import Place


class Faction(BaseModel):
    """
    A faction is a group of people sharing and working towards a common objective.
    A Character may be or may not be affiliated with one or many Factions.
    A faction can have a specific place as HQ
    """
    name = models.CharField(max_length=100, help_text="E.g. Avengers, Starfleet, Jedi Order etc.")
    description = models.TextField(help_text="Some words about the faction.")

    objective = models.CharField(max_length=500, help_text="E.g. Protecting Earth, Maintaining Peace etc.")

    headquarter = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="factions_associated")

    def __str__(self):
        return self.name

