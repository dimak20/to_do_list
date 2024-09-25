from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from to_do_management.views import TaskListView, TaskCreateView

app_name = "management"

urlpatterns = [
    path("", TaskListView, name="home"),
    path("tasks/create/", TaskCreateView, name="task-create"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)