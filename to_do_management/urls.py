from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from to_do_management.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView, \
    TagUpdateView, TagDeleteView, TagCreateView, TagListView, change_status

app_name = "management"

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/", TaskDetailView.as_view(), name="tag-detail"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/<int:pk>/change_status", change_status, name="task-change"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)