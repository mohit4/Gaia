from django.db import models

from base.models import BaseModel
from faction.models import Faction
from place.models import Place, Event


class Character(BaseModel):
    """
    Any living person, creature, robot, walking or non-walking entity with consciousness identifies as
    a character.
    """
    firstname = models.CharField(max_length=50, help_text="E.g. Harry, Jon, Steve etc.")
    lastname = models.CharField(max_length=50, help_text="E.g. Potter, Snow, Rogers etc.")
    aliases = models.CharField(max_length=200, null=True, blank=True, help_text="You can add more than one using comma(,)")

    age = models.PositiveIntegerField(help_text="Age in years")

    appearance = models.TextField(help_text="Details about physical appearance.")
    behaviour = models.TextField(help_text="Details about mental behaviour.")

    factions = models.ManyToManyField(Faction, related_name="members")
    origin = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="characters_associated")
    events = models.ManyToManyField(Event, related_name="characters_associated", blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
