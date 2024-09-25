from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from to_do_management.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

app_name = "management"

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)