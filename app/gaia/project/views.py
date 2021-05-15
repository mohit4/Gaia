from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Project


class Homepage(TemplateView):
    """
    Main Page
    """
    template_name = "project/homepage.html"


class Dashboard(TemplateView):
    """
    Dashboard for a user
    """
    template_name = "project/dashboard.html"


class ProjectListView(ListView):
    """
    Listing all the project
    """
    template_name = 'project/project_list.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    """
    Details of a project
    """
    template_name = 'project/project_detail.html'
    model = Project
    context_object_name = 'project'


class ProjectCreateView(SuccessMessageMixin, CreateView):
    """
    Creating a new project
    """
    template_name = 'project/project_create.html'
    model = Project
    fields = ('title', 'description', 'user')
    success_message = 'New project created!'


class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    """
    Updating a new project
    """
    template_name = 'project/project_update.html'
    model = Project
    fields = ('description',)
    success_message = 'Project updated!'


class ProjectDeleteView(DeleteView):
    """
    Deleting an existing project
    """
    template_name = 'project/project_detail.html'
    model = Project
    success_url = reverse_lazy('project:project-list')
