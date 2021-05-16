from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Place


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