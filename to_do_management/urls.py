from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from to_do_management.views import TaskListView, TaskCreateView

app_name = "management"

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)