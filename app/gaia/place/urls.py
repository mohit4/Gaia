from django.urls import path

from .views import PlaceListView, PlaceUpdateView, PlaceCreateView, PlaceDeleteView, PlaceDetailView

app_name = 'place'

urlpatterns = [
    path('place/all/', PlaceListView.as_view(), name='place-list'),
    path('place/<int:pk>', PlaceDetailView.as_view(), name='place-detail'),
    path('place/create/', PlaceCreateView.as_view(), name='place-create'),
    path('place/<int:pk>/update/', PlaceUpdateView.as_view(), name='place-update'),
    path('place/<int:pk>/delete/', PlaceDeleteView.as_view(), name='place-delete'),
]
