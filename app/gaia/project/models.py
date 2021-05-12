from django.db import models
from django.contrib.auth.models import User

from base.models import BaseModel


class Project(BaseModel):
    """
    A Gaia project is the leading entity that a user can create.
    All elements will be associated with a project.
    """

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title