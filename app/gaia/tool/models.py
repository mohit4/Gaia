from django.db import models

from base.models import BaseModel


class Ability(BaseModel):
    """
    A specific use for a tool
    """
    
    text = models.CharField(max_length=100, help_text="E.g. To navigate, For Healing etc.")

    def __str__(self):
        return self.text


class Tool(BaseModel):
    """
    A tool is an equipment that allows the holder or user a special ability
    to carry out a task.
    """

    name = models.CharField(max_length=50, help_text="E.g. Navigator, Magic Wand, Inverter cell etc.")
    description = models.TextField(help_text="Some words about this tool.")

    abilities = models.ManyToManyField(Ability, related_name="tools")

    def __str__(self):
        return self.name


class Weapon(BaseModel):
    """
    A weapon is a tool or equipment specifically used for destructive or military purposes
    """

    name = models.CharField(max_length=50, help_text="E.g. Iron Man Suit, Agni V, Plasma Gun etc.")
    description = models.TextField(help_text="Some words about this weapons.")

    abilities = models.ManyToManyField(Ability, related_name="weapons")

    def __str__(self):
        return self.name
