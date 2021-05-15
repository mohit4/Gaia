from django.urls import path

from .views import Homepage
from .views import Dashboard
from .views import ProjectListView, ProjectUpdateView, ProjectCreateView, ProjectDeleteView, ProjectDetailView
from .views import ReferenceListView, ReferenceUpdateView, ReferenceCreateView, ReferenceDeleteView, ReferenceDetailView

app_name = 'project'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('project/', Dashboard.as_view(), name='dashboard'),
    path('project/all/', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('reference/all/', ReferenceListView.as_view(), name='reference-list'),
    path('reference/<int:pk>', ReferenceDetailView.as_view(), name='reference-detail'),
    path('reference/create/', ReferenceCreateView.as_view(), name='reference-create'),
    path('reference/<int:pk>/update/', ReferenceUpdateView.as_view(), name='reference-update'),
    path('reference/<int:pk>/delete/', ReferenceDeleteView.as_view(), name='reference-delete'),
]
