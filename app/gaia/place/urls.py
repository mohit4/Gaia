from django.urls import path

from .views import PlaceListView, PlaceUpdateView, PlaceCreateView, PlaceDeleteView, PlaceDetailView
from .views import EventListView, EventUpdateView, EventCreateView, EventDeleteView, EventDetailView

app_name = 'place'

urlpatterns = [
    path('place/all/', PlaceListView.as_view(), name='place-list'),
    path('place/<int:pk>', PlaceDetailView.as_view(), name='place-detail'),
    path('place/create/', PlaceCreateView.as_view(), name='place-create'),
    path('place/<int:pk>/update/', PlaceUpdateView.as_view(), name='place-update'),
    path('place/<int:pk>/delete/', PlaceDeleteView.as_view(), name='place-delete'),
    path('event/all/', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]
