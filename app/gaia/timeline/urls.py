from django.urls import path

from .views import TimelineListView, TimelineUpdateView, TimelineCreateView, TimelineDeleteView, TimelineDetailView

app_name = 'timeline'

urlpatterns = [
    path('timeline/all/', TimelineListView.as_view(), name='timeline-list'),
    path('timeline/<int:pk>', TimelineDetailView.as_view(), name='timeline-detail'),
    path('timeline/create/', TimelineCreateView.as_view(), name='timeline-create'),
    path('timeline/<int:pk>/update/', TimelineUpdateView.as_view(), name='timeline-update'),
    path('timeline/<int:pk>/delete/', TimelineDeleteView.as_view(), name='timeline-delete'),
]
