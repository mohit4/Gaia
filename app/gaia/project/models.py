from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from base.models import BaseModel


class Reference(BaseModel):
    """
    A reference is a short note on any term introduced in any project
    """
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project:reference-detail", kwargs={"pk": self.pk})


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
    
    def get_absolute_url(self):
        return reverse("project:project-detail", kwargs={"pk": self.pk})
