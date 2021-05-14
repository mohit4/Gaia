from django.db.models.deletion import CASCADE
from timeline.models import Timeline
from django.db import models

from base.models import BaseModel
from place.models import Place


class Currency(BaseModel):
    """
    A currency system that is used throughout a system or place for trading.
    """
    name = models.CharField(max_length=50, help_text="E.g. BitCoin, Rupee, Dollar etc.")
    description = models.TextField(help_text="Few words about the currency.")

    effective_place = models.ManyToManyField(Place)

    def __str__(self):
        return self.name


class Resource(BaseModel):
    """
    A valuable resource that can be traded for a certain amount of currency.
    """
    name = models.CharField(max_length=50, help_text="E.g. Vibranium, Pym Particles, Energons etc.")
    description = models.TextField(help_text="Few words about the resource.")

    value = models.PositiveIntegerField(help_text="Numerical value of the currency in which 1 Unit of resource can be traded.")
    
    origin = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="resources", help_text="Place where the resource can be found!")
    accepted_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="tradable_resources", help_text="Name of the currency in which resource can be traded.")

    def __str__(self):
        return f"{self.name} : {self.value} {self.accepted_currency.name}(s) per unit"
