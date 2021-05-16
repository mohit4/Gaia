from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Timeline


class TimelineListView(ListView):
    """
    Listing all the timeline
    """
    template_name = 'timeline/timeline_list.html'
    model = Timeline
    context_object_name = 'timelines'


class TimelineDetailView(DetailView):
    """
    Details of a timeline
    """
    template_name = 'timeline/timeline_detail.html'
    model = Timeline
    context_object_name = 'timeline'


class TimelineCreateView(SuccessMessageMixin, CreateView):
    """
    Creating a new timeline
    """
    template_name = 'timeline/timeline_create.html'
    model = Timeline
    fields = ('era', 'start_period', 'end_period', 'label', 'project')
    success_message = 'New timeline created!'


class TimelineUpdateView(SuccessMessageMixin, UpdateView):
    """
    Updating a new timeline
    """
    template_name = 'timeline/timeline_update.html'
    model = Timeline
    fields = ('start_period', 'end_period', 'label',)
    success_message = 'Timeline updated!'


class TimelineDeleteView(DeleteView):
    """
    Deleting an existing timeline
    """
    template_name = 'timeline/timeline_detail.html'
    model = Timeline
    success_url = reverse_lazy('timeline:timeline-list')