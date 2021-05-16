from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Place
from .models import Event


class PlaceListView(ListView):
    """
    Listing all the place
    """
    template_name = 'place/place_list.html'
    model = Place
    context_object_name = 'places'


class PlaceDetailView(DetailView):
    """
    Details of a place
    """
    template_name = 'place/place_detail.html'
    model = Place
    context_object_name = 'place'


class PlaceCreateView(SuccessMessageMixin, CreateView):
    """
    Creating a new place
    """
    template_name = 'place/place_create.html'
    model = Place
    fields = ('name', 'description', 'domain', 'timeline',)
    success_message = 'New place created!'


class PlaceUpdateView(SuccessMessageMixin, UpdateView):
    """
    Updating a new place
    """
    template_name = 'place/place_update.html'
    model = Place
    fields = ('description', 'domain', 'timeline',)
    success_message = 'Place updated!'


class PlaceDeleteView(DeleteView):
    """
    Deleting an existing place
    """
    template_name = 'place/place_detail.html'
    model = Place
    success_url = reverse_lazy('place:place-list')


class EventListView(ListView):
    """
    Listing all the event
    """
    template_name = 'place/event_list.html'
    model = Event
    context_object_name = 'events'


class EventDetailView(DetailView):
    """
    Details of a event
    """
    template_name = 'place/event_detail.html'
    model = Event
    context_object_name = 'event'


class EventCreateView(SuccessMessageMixin, CreateView):
    """
    Creating a new event
    """
    template_name = 'place/event_create.html'
    model = Event
    fields = ('heading', 'description', 'time_started', 'time_ended', 'place',)
    success_message = 'New event created!'


class EventUpdateView(SuccessMessageMixin, UpdateView):
    """
    Updating a new event
    """
    template_name = 'place/event_update.html'
    model = Event
    fields = ('description', 'time_started', 'time_ended', 'place',)
    success_message = 'Event updated!'


class EventDeleteView(DeleteView):
    """
    Deleting an existing event
    """
    template_name = 'place/event_detail.html'
    model = Event
    success_url = reverse_lazy('event:event-list')
