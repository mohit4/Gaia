from django.urls import path

from .views import Homepage
from .views import Dashboard
from .views import ProjectListView, ProjectUpdateView, ProjectCreateView, ProjectDeleteView, ProjectDetailView

app_name = 'project'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('project/', Dashboard.as_view(), name='dashboard'),
    path('project/all/', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]
