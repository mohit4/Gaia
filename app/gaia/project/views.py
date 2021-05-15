from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Project
from .models import Reference


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


class ReferenceListView(ListView):
    """
    Listing all the references
    """
    template_name = 'project/reference_list.html'
    model = Reference
    context_object_name = 'references'


class ReferenceDetailView(DetailView):
    """
    Details of a reference
    """
    template_name = 'project/reference_detail.html'
    model = Reference
    context_object_name = 'reference'


class ReferenceCreateView(SuccessMessageMixin, CreateView):
    """
    Creating a new reference
    """
    template_name = 'project/reference_create.html'
    model = Reference
    fields = ('title', 'description')
    success_message = 'New reference created!'


class ReferenceUpdateView(SuccessMessageMixin, UpdateView):
    """
    Updating a new reference
    """
    template_name = 'project/reference_update.html'
    model = Reference
    fields = ('description',)
    success_message = 'Reference updated!'


class ReferenceDeleteView(DeleteView):
    """
    Deleting an existing reference
    """
    template_name = 'project/reference_detail.html'
    model = Reference
    success_url = reverse_lazy('project:reference-list')
